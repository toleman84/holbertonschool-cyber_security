#!/bin/bash
sudo nmap -p 22,80,443 -sn -sS $1
