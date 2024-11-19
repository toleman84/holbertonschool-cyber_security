#!/bin/bash
awk '{print$1}' | uniq -d $1 | sort | head -n 1 | cut -c 1-12
