#!/bin/bash
echo -n "$1$(openssl rand -base64 16)" | openssl dgst -sha512 | awk '{print}' > 3_hash.txt
