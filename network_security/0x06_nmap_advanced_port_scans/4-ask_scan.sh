#!/bin/bash
sudo nmap -sA -reason -p $2 -host-timeout 1000m $1
