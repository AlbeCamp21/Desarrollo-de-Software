#!/usr/bin/env bash

# stdout a archivo txt
ls -l > listado.txt
# stderr
grep f1 *.log 2> errores.log
# ambos
make &> build.log
# pipe
ps aux | grep sshd | awk '{print $2}'
# process substitution
diff <(sort hello.sh) <(sort array.sh)
