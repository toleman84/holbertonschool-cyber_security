#!/bin/bash
find "$1" \( -perm -4000 -o -perm -2000 \) -type f 2>/dev/null -mtime -1 -exec ls -l {} \;
