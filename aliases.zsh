#!/usr/bin/env zsh

translate() {
  TMP=$(mktemp)
  cliaiai --output "$TMP" translate "$@"
  cat "$TMP" | pbcopy
  rm "$TMP"
}

howto() {
    TMP=$(mktemp)
    cliaiai --output "$TMP" command "$@"
    COMMAND=$(< "$TMP")
    rm "$TMP"
    print -rz $COMMAND
}