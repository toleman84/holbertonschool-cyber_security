#!/bin/bash
sudo nmap -sA -reason -p $2 -T1 $1
