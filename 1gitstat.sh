#!/bin/bash

#TODO git test if git msg || skip

for dir in */; do
    if [[ -d "$dir" ]]; then
        cd "$dir"
        for dir2 in */; do
            if [[ -d "$dir2" ]]; then
                cd "$dir2"
                ls -d "$PWD"/*
                cd ..
            fi
        done
        cd ..
    fi
done

