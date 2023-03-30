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
function init {
    if [[ -f "${HOME}/.gitstat.ini" ]]; then
        tmp="$(grep location .gitstat.ini)"
        return "${tmp##location = }"
    fi
    #TODO file
}
function main {
    local CDIR
    CDIR=$(pwd)
    local WDIR
    WDIR=init #"/home/adrian/gits"
    getinfo

    find "${WDIR}" -type d -name ".git" -prune -print0 | while IFS= read -r -d '' repo; do
        cd "${repo%/*}" && getstat
    done

    cd "${CDIR}" >"/dev/null" || return
}
main "${@}"
