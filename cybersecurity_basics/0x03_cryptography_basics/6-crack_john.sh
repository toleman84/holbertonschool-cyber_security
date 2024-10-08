#!/bin/bash
john --wordlist=/usr/share/wordlists/rockyou.txt --format=Raw-SHA256 --fork=4 "$1"
