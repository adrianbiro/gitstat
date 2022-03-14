#!/bin/bash

#TODO git test if git msg || skip
function gitstat() {
  git status -sb
}

function subtest(){

  for dir2 in */
  do
    if [[ -d "$dir2" ]]; then
      (
      cd "$dir2" || return
        if [[ -d ".git" ]]; then
          gitstat
 #       else
 #         continue
        fi
        )
    fi
  done
}

function main(){
  local CDIR; CDIR=$(pwd)
  local WDIR; WDIR="/home/adrian/bin/gits"
  cd $WDIR || return
  for dir in */
  do
    if [[ -d "$dir" ]]; then
      (
      cd "$dir" || return
        if [[ -d ".git" ]]; then
          gitstat
        else
          subtest
        fi
        )
    fi
  done
  cd "$CDIR" || return
  exit 0
}

main "$@"
