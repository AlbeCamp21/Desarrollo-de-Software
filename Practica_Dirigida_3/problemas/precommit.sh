#!/usr/bin/env bash

set -euo pipefail

# Hook pre commit para realizar verificaciones antes de confirmar cambios
# Verifica:
# - comentarios TODO/FIXME en estos archivos: .sh, .py, .js
# - errores de sintaxis con shellcheck para archivos .sh
# - errores con pyflakes para archivos .py
# Tambien, genera un reporte del estado del repositorio si se pasan las verificaciones

# variables globales
declare -a errors=()
has_errors=false
skip_report=false

# verifica si se pasa el flag --skip-report
if [[ "$*" == *--skip-report* ]]; then
    skip_report=true
fi

# Funcion para verificar comentarios TODO/FIXME
check_todo_comments() {
    echo "Verificando comentarios TODO/FIXME..."
    local staged_files
    mapfile -t staged_files < <(git diff --cached --name-only --diff-filter=ACM | grep -E '\.(sh|py|js)$')
    
    for file in "${staged_files[@]}"; do
        if [[ ! -f "$file" ]]; then
            continue
        fi
        
        local todos
        todos=$(grep -En '(TODO|FIXME)' "$file" || true)
        
        if [[ -n "$todos" ]]; then
            has_errors=true
            errors+=("Archivo: $file contiene TODO/FIXME:")
            while IFS= read -r line; do
                errors+=("  $line")
            done <<< "$todos"
        fi
    done
}

# Funcion para ejecutar shellcheck en archivos .sh
run_shellcheck() {
    echo "Ejecutando shellcheck..."
    local staged_sh_files
    mapfile -t staged_sh_files < <(git diff --cached --name-only --diff-filter=ACM | grep -E '\.sh$')
    
    for file in "${staged_sh_files[@]}"; do
        if [[ ! -f "$file" ]]; then
            continue
        fi
        
        local output
        if ! output=$(shellcheck -f gcc "$file" 2>&1); then
            has_errors=true
            errors+=("Errores de shellcheck en $file:")
            while IFS= read -r line; do
                errors+=("  $line")
            done <<< "$output"
        fi
    done
}

# Funcion para ejecutar pyflakes en archivos .py
run_pyflakes() {
    echo "Ejecutando pyflakes..."
    local staged_py_files
    mapfile -t staged_py_files < <(git diff --cached --name-only --diff-filter=ACM | grep -E '\.py$')
    
    for file in "${staged_py_files[@]}"; do
        if [[ ! -f "$file" ]]; then
            continue
        fi
        
        local output
        if ! output=$(pyflakes "$file" 2>&1); then
            has_errors=true
            errors+=("Errores de pyflakes en $file:")
            while IFS= read -r line; do
                errors+=("  $line")
            done <<< "$output"
        fi
    done
}

# Funcion para generar reporte
generate_report() {
    if $skip_report; then
        echo "Reporte omitido (--skip-report)"
        return
    fi
    
    local report_file="precommit_report_$(date +%Y%m%d_%H%M%S).txt"
    {
        echo "==== Reporte Pre-Commit ===="
        echo "Fecha: $(date)"
        echo "Rama: $(git rev-parse --abbrev-ref HEAD)"
        echo ""
        echo "==== Archivos staged ===="
        git diff --cached --name-only --diff-filter=ACM
        echo ""
        echo "==== Estado del repositorio ===="
        git status --short
        echo ""
        
        if [[ ${#errors[@]} -gt 0 ]]; then
            echo "==== Errores detectados ===="
            printf '%s\n' "${errors[@]}"
        fi
    } > "$report_file"
    
    echo "Reporte generado en $report_file"
}

# manejar errores
trap 'echo "Error en hook pre-commit en la línea $LINENO"; exit 1' ERR

# ejecutar verificaciones
check_todo_comments
run_shellcheck
run_pyflakes

# se toma decisión basada en los resultados
if $has_errors; then
    echo "===== Errores encontrados ====="
    printf '%s\n' "${errors[@]}"
    echo "Commit abortado por errores"
    exit 1
else
    generate_report
    exit 0
fi
