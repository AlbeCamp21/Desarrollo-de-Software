# Hook Pre-Commit para Control de Calidad

Este hook realiza verificaciones automáticas antes de cada commit para mantener la calidad del código.

## Requisitos

- Bash
- shellcheck
- pyflakes

## Instalación
- Instalar dependencias en Ubuntu/Debian:
```bash
sudo apt-get install shellcheck pyflakes
```
- Copiar el contenido de `precommit.sh` en el hook `.git/hooks/pre-commit`

## Ejemplo
### Commit aprobado
```bash
echo "Código limpio" > ejemplo.sh
git add ejemplo.sh
git commit -m "Agrega script válido"
```
#### Salida:
```
Verificando comentarios TODO/FIXME...
Ejecutando shellcheck...
Ejecutando pyflakes...
Reporte generado en precommit_report.txt
[main 1111111] Agrega script válido
 1 file changed, 1 insertion(+)
```

### Commit rechazado
```bash
echo "# TODO: Implementar función" > problema.py
git add problema.py
git commit -m "WIP"
```
#### Salida:
```
Verificando comentarios TODO/FIXME...
=== Errores encontrados ===
Archivo: problema.py contiene TODO/FIXME:
  1:# TODO: Implementar función
Commit abortado por errores
```


- El hook verifica:
  - Comentarios TODO/FIXME (.sh, .py, .js)
  - Errores con shellcheck (.sh)
  - Problemas con pyflakes (.py)
  - Genera reporte automático (a menos que uses --skip-report)
