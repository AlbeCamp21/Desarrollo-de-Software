#!/usr/bin/env bash

# for clásico
for ((i=1;i<=3;i++)); do echo "Iter $i"; done

# for-in
for file in *.sh; do echo "Script: $file"; done

# while
count=3
while (( count>0 )); do echo "$count"; ((count--)); done

# until
until [[ -f listado.txt ]]; do sleep 1; done
echo "listado.txt listo"
