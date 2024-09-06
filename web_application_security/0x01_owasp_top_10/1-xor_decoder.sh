#/bin/bash
pass="$1"
pass="${pass#'{xor}'}"
decoded=$(echo "$pass" | base64 -d)

decoded_pass_xor=""
for ((i = 0; i < ${#decoded}; i++)); do
    char="${decoded:$i:1}"
    ascii_value=$(printf "%d" "'$char")
    xor_result=$(( ascii_value ^ 95 ))
    decoded_pass_xor+="$(printf "$(printf '\\x%x' $xor_result)")"
done

echo -e "$decoded_pass_xor"
