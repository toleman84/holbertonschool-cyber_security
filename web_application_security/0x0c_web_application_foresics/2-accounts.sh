#!/bin/bash
tail -n 1000 auth.log | grep -E "root" | awk '{print $11}' | tail -n 1
