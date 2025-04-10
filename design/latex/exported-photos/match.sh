#!/bin/bash

target_directory=../photos/
source_file_extension=".png"
target_file_extension=".jpg"

for file in *"${source_file_extension}"; do
    base_name="${file%$source_file_extension}"
    target_file="$(find ../photos/ -maxdepth 2 -type d -iname "${base_name}")"
    if [ -d "$target_file" ]; then
        target_file="${target_file}/${base_name}${target_file_extension}"
        # echo "Converting $file to $target_file"
        convert "$file" "$target_file"
    else
        echo "${file}"
    fi
done
