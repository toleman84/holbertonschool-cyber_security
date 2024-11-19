#!/bin/bash
awk '{print $1}' $1 | uniq -c | sort -nr | head -n 1 | awk '{print $2}'
