#!/usr/bin/env bash

# if
num=$1
if [[ -z $num ]]; then
  echo "Pasa un número"
  exit 1
elif (( num % 2 == 0 )); then
  echo "$num es par"
else
  echo "$num es impar"
fi


# case
ext="$2"
case "$ext" in
  txt) echo "Texto" ;;
  sh)  echo "Shell" ;;
  py)  echo "Python" ;;
  *)   echo "Desconocido" ;;
esac
