#!/bin/bash
sudo nmap -sA -reason -p $2 -host-tmeout 1000m $1
