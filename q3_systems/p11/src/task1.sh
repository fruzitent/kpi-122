#!/usr/bin/env bash

print_gt() {
    length=${1}
    args=${@:2}
    for arg in ${args}; do
        if [ ${#arg} -gt ${length} ]; then
            echo $arg
        fi
    done
}

print_gt ${1} ${2}
