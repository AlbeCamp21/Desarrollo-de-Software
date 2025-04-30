#!/usr/bin/env bash

echo "Lista de archivos:"
find . -type f -exec stat --format '%y %n' {} + | sort

echo -e "\nArchivo más reciente:"
find . -type f -exec stat --format '%Y %n' {} + | sort -n | tail -n 1 | cut -d' ' -f2- | xargs stat --format='%y %n'
