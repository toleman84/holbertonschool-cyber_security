#!/bin/bash
john --wordlist=/usr/share/wordlists/rockyou.txt --format=nt --fork=4 "$1"
