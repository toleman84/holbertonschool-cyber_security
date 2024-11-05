#!/bin/bash
sudo nmap -p $2 $1 &> custom_scan.txt
