#!/bin/bash
sudo nmap -sn -p 22,80,443 -sA $1
