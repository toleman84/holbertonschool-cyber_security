#!/bin/bash
ps -U "$1" -u "$1" -o user,pid,%cpu,%mem,vsz,rss,tty,stat,started,time,cmd | awk '$5 > 0' | awk '$6 > 0'
