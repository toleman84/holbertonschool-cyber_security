#/bin/bash
decoded=$(echo "$1" | base64 -d)

key=$(echo -n "test" | xxd -p)

decoded_text=$(echo -n "$decoded" | xxd -p | awk -v key="$key" '
  BEGIN {
    split(key, k, "")
    for (i = 1; i <= length(k); i += 2) {
      k[i] = strtonum("0x" k[i] k[i + 1])
    }
  }
  {
    split($0, b, "")
    for (i = 1; i <= length(b); i += 2) {
      byte = strtonum("0x" b[i] b[i + 1])
      xor = byte ^ k[(i - 1) % length(k) + 1]
      printf("%c", xor)
    }
  }
')

echo "$decoded_text"
