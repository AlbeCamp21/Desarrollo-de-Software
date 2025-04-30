#!/usr/bin/env bash

marco() {
  export MARCO_DIR="$PWD"
}

polo() {
  if [[ -z "$MARCO_DIR" ]]; then
    echo "No se ha ejecutado el comando 'marco' aún."
    return 1
  fi
  cd "$MARCO_DIR" || return 1
}
