#!/bin/bash

function getinfo {
    printf "Status overview of local git repositories from: %s\nOwned by: %s\n\n" "${WDIR}" "$(git config user.name)"
}
function getstat() {
    if [[ -n "$(git status --porcelain)" ]]; then
        echo "${PWD}"
        git status -sb
    fi
}

function main {
    local CDIR
    CDIR=$(pwd)
    local WDIR
    WDIR="${GITS:?"To run ${0##*/} export GITS=/path/to/all/repos"}"
    
    getinfo

    find "${WDIR}" -type d -name ".git" -prune -print0 | while IFS= read -r -d '' repo; do
        cd "${repo%/*}" && getstat
    done

    cd "${CDIR}" >"/dev/null" || return
}
main "${@}"
