#!/usr/bin/python3
import subprocess
import os
from datetime import datetime

LOCATION = "/home/adrian/gits"  # The central location for git repos.
todo = []

def get_stat(path):
    os.chdir(path)
    status = subprocess.run(["git", "status", "-sb"], capture_output=True, text=True)
    if len(status.stdout.replace("\n", "").split(" ")) > 2:  # 2 = nothing to commit
        todo.append("42424242")
        print("\n" + os.getcwd())
        status = subprocess.run(["git", "status", "-sb"])

def get_info():
    user_name = subprocess.run(["git", "config", "user.name"], capture_output=True, text=True)
    user_name = user_name.stdout.replace("\n", "")
    time_stamp = datetime.now()
    print(f"{time_stamp}\nStatus overview of local git repositories from: {LOCATION}\nOwned by {user_name}.")

def main():
    """No matter how deep in the directory structure are repos placed, unlike the earlier bash version, this will easily scan all, without too verbose output. """
    get_info()
    for (root, dirs, files) in os.walk(LOCATION):
        if ".git" in os.listdir(root):
            get_stat(root)
    if not todo:
        print("There is nothing to do.")
main()







"""
old bash version


function getinfo() {
  local mdate; mdate=$(date +'%Y-%m-%d-%T')
  local username; username=$(git config user.name)
  clear
  printf '\e[31;5m%s\033[0m\n\e[21m%s\033[0m\n\e[36m%s\033[0m\n\n' "!GIT!" "$mdate" "Status overview of local git repositories from $WDIR owned by $username"
}


function getstat() {
  local lines; lines=$(git status -bs | wc -l)
  local localwd; localwd=$(pwd)

  if [[ "$lines" -eq 1 ]]; then
    total+=("$(pwd)")
  else
    commit+=("$(pwd)")
  fi
  git status -sb
}


function main(){
  local CDIR; CDIR=$(pwd)
  local WDIR; WDIR="/home/adrian/gits"
  declare -a commit; commit=("")
  declare -a total; total=("")
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
  getmodrepos
  cd "$CDIR" || return
  exit 0
}

main "$@"
"""
