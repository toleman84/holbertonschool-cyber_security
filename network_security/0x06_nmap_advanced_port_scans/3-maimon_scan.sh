#!/bin/bash
sudo nmap -sM -p http*,ftp,ssh,telnet -v $1
