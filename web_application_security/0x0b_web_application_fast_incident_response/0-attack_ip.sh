#!/bin/bash
url="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/text/2024/6/0090562cfd09781b394bfd9a051ca2f769e48c54.txt?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20241119%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20241119T132137Z&X-Amz-Expires=345600&X-Amz-SignedHeaders=host&X-Amz-Signature=3449cd0a4b6a9833e03f33169b73f44e796dcd9a849020a600ab96541dbc0fc9"
output_file="logs.txt"
curl -o "$output_file" "$url"
awk '{print $1}' "$output_file" | uniq -c | sort -nr | head -n 1 | awk '{print $2}'
