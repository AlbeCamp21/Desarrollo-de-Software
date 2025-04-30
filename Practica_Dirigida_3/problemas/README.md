# Script de Limpieza de Git: clean_git.sh

Este script Bash automatiza la limpieza de ramas y stashes en repositorios Git

## Requisitos
- Bash
- Git
- jq (para generación de JSON)

## Uso

```bash
./clean_git.sh [OPCIÓN]
```

## Opciones disponibles:
- --branches: Limpiar ramas locales y remotas
- --stashes: Gestionar stashes (aplicar o eliminar)
- --backup: Crear backup del reflog
- --report: Generar informe en formato JSON
- --help: Mostrar ayuda
- --debug: Activar modo depuración
