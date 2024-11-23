#!/bin/bash
grep "new user" auth.log | awk '{print $(NF-4)}' | tr -d "," | cut -d= -f2 | sort | paste -sd,
