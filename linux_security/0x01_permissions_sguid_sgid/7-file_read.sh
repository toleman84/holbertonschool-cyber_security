#!/bin/bash
find "$1" -type f 2>/dev/null -exec chmod o=r {} \;
