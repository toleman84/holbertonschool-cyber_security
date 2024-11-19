#!/bin/bash
uniq -d $1 | cut -c 1-12 | head -n 1
