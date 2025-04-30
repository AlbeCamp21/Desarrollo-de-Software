#!/usr/bin/env bash

set -euo pipefail

# ayuda para el usuario
mostrar_ayuda() {
    cat << EOF
Uso: $0 [OPCIÓN]

Opciones:
  --branches     Limpiar ramas locales y remotas
  --stashes      Gestionar stashes (aplicar o eliminar)
  --backup       Crear backup del reflog
  --report       Generar informe en formato JSON
  --help         Mostrar esta ayuda
  --debug        Activar modo depuración

Ejemplos:
  $0 --branches
  $0 --stashes
  $0 --backup
EOF
}

# Funcion para limpiar ramas locales y remotas
limpiar_ramas() {
    echo "Introduce un patrón de expresión regular para filtrar ramas (ej. feature/.* o bugfix/.*):"
    read -r patron
    
    # Validando el patrón introducido
    if ! [[ $patron =~ ^[[:alnum:]_/.-]+$ ]]; then
        echo "Error: '$patron' no es válido." >&2
        exit 1
    fi
    
    # ramas locales
    echo "===== Ramas locales que coinciden con '$patron' ====="
    local -a ramas_locales=()
    mapfile -t ramas_locales < <(git branch | grep -E "$patron" | sed 's/^\*? *//')
    
    if [[ ${#ramas_locales[@]} -eq 0 ]]; then
        echo "No hay ramas locales que coincidan con '$patron'"
    else
        for rama in "${ramas_locales[@]}"; do
            echo "¿Eliminar rama local '$rama'? (s/n)"
            read -r respuesta
            if [[ $respuesta =~ ^[sS]$ ]]; then
                git branch -D "$rama" && echo "Rama '$rama' eliminado."
            fi
        done
    fi
    
    # ramas remotas
    echo "===== Ramas remotas que coinciden con '$patron' ====="
    local -a ramas_remotas=()
    mapfile -t ramas_remotas < <(git branch -r | grep -E "$patron" | sed 's/^ *origin\///' | grep -v 'HEAD ->')
    
    if [[ ${#ramas_remotas[@]} -eq 0 ]]; then
        echo "No hay ramas remotas que coincidan con '$patron'"
    else
        for rama in "${ramas_remotas[@]}"; do
            echo "¿Eliminar rama remota '$rama'? (s/n)"
            read -r respuesta
            if [[ $respuesta =~ ^[sS]$ ]]; then
                git push origin --delete "$rama" && echo "Rama remota '$rama' eliminada."
            fi
        done
    fi
}

# Función para gestionar stashes
gestionar_stashes() {
    echo "===== Lista de stashes ====="
    local lista_stashes
    lista_stashes=$(git stash list | nl -w2 -s'. ')
    
    if [[ -z "$lista_stashes" ]]; then
        echo "No hay stashes disponibles."
        return
    fi
    
    echo "$lista_stashes"
    echo "Introduce los índices de los stashes a gestionar (separados por espacios):"
    read -r indices
    
    # Validando índices
    local -a arr_indices=($indices)
    for i in "${arr_indices[@]}"; do
        if ! [[ $i =~ ^[0-9]+$ ]]; then
            echo "Error: Índice '$i' no válido." >&2
            exit 1
        fi
    done
    
    echo "¿Qué acción deseas realizar? (aplicar/eliminar)"
    read -r accion
    
    for i in "${arr_indices[@]}"; do
        echo "¿${accion^} stash@{$i}? (s/n)"
        read -r respuesta
        if [[ $respuesta =~ ^[sS]$ ]]; then
            if [[ $accion == "aplicar" ]]; then
                git stash apply "stash@{$i}"
            else
                git stash drop "stash@{$i}"
            fi
        fi
    done
}

# Funcion para crear backup del reflog
backup_reflog() {
    local archivo="reflog_$(date +%Y%m%d_%H%M%S).log"
    git reflog | grep -E "reset|merge" > "$archivo"
    echo "Backup del reflog guardado en $archivo"
}

# Funcion para generar informe JSON
informe_json() {
    local rama_actual=$(git rev-parse --abbrev-ref HEAD)
    local cantidad_stashes=$(git stash list | wc -l)
    local tags=$(git tag | jq -R -s -c 'split("\n")[:-1]')
    local submodulos=$(git submodule status | awk '{print $2}' | jq -R -s -c 'split("\n")[:-1]')
    
    local json
    json=$(cat << EOF
{
    "rama_actual": "$rama_actual",
    "cantidad_stashes": $cantidad_stashes,
    "tags": $tags,
    "submodulos": $submodulos
}
EOF
    )
    
    local archivo="informe_$(date +%Y%m%d).json"
    echo "$json" > "$archivo"
    echo "Informe JSON generado en $archivo"
}

# Validar opciones
if [[ $# -eq 0 ]]; then
    mostrar_ayuda
    exit 1
fi

case $1 in
    --branches)
        limpiar_ramas
        ;;
    --stashes)
        gestionar_stashes
        ;;
    --backup)
        backup_reflog
        ;;
    --report)
        informe_json
        ;;
    --help)
        mostrar_ayuda
        ;;
    --debug)
        set -x
        export PS4='+ ${BASH_SOURCE}:${LINENO}:${FUNCNAME[0]}: '
        ;;
    *)
        echo "Opción no válida: $1" >&2
        mostrar_ayuda
        exit 1
        ;;
esac
