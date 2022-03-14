#!/bin/bash

function getstat() {
  local lines; lines=$(git status -bs | wc -l)
  declare -a commit; commit=("")
  declare -a total; total=("")
  local lastdir; lastdir=$(find "$WDIR" -maxdepth 1 -mindepth 1 -type d -printf '%f\n' | sort -r | awk 'NR==1 {print $0}')
  local localwd; localwd=$(pwd)
  local formtotal; formtotal=${total[-1]}
  local formlocalwd; formlocalwd=${localwd:22}

  if [[ "$lines" -eq 1 ]]; then
    total+=("$(pwd)")
  else
    commit+=("$(pwd)")
  fi
  git status -sb
  echo "$formtotal $formlocalwd $lastdir"
  if [[ "$lastdir" = "$formlocalwd" ]]; then
    for i in "${commit[@]}"
    do
      printf '%s\n' ${i:22}
    done
  fi
}


function getinfo() {
  local mdate; mdate=$(date +'%Y-%m-%d-%T')
  local username; username=$(git config user.name)
  clear
  printf '\e[31;5m%s\033[0m\n\e[21m%s\033[0m\n\e[36m%s\033[0m\n\n' "!GIT!" "$mdate" "Status overview of local git repositories from $WDIR owned by $username"
}


function main(){
  local CDIR; CDIR=$(pwd)
  local WDIR; WDIR="/home/adrian/bin/gits"
  cd $WDIR || return
  getinfo
  for dir in */
  do
    if [[ -d "$dir" ]]; then
      (
      cd "$dir" || return
        if [[ -d ".git" ]]; then
          getstat
        else
        for dir2 in */
        do
          if [[ -d "$dir2" ]]; then
            (
            cd "$dir2" || return
              if [[ -d ".git" ]]; then
                getstat
              fi
              )
          fi
        done
        fi
        )
    fi
  done
  cd "$CDIR" || return
  exit 0
}

main "$@"
