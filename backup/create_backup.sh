#!/usr/bin/env bash

read -r dir_name < ./folder_name.txt

for dir in "/mnt/z/$dir_name"/*/; do
  for item in $dir/*/; do
    # Remove everything up to and including the "//"
    item=$(echo "$item" | sed 's/^.*\/\///')
    # Ignore lines that have a */ directly after the double //
    if [[ $item != *"*/" ]] && [[ $item != "Subs/" ]] && [[ $item != "Sample/" ]]; then
      # Remove the trailing slash
      item=$(echo "$item" | tr -d '/')
      echo "$item" >> $1
    fi
  done
done
