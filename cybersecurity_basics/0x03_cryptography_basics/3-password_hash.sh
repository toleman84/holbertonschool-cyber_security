#!/bin/bash
string="$1"
rand_string=$(openssl rand -base64 16)
passwd=$rand_string$string
hash=$(echo -n "$passwd" | openssl dgst -sha512)
echo "$hash" > 3_hash.txt
