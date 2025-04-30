#!/usr/bin/env bash

contador=0

while true; do
  ((contador++))
  ./error_comando.sh >out.txt 2>error.txt
  if [[ $? -ne 0 ]]; then
    echo "El comando falló luego de $contador ejecuciones."
    echo -e "\n--- OUT ---"
    cat out.txt
    echo -e "\n--- ERROR ---"
    cat error.txt
    break
  fi
done
