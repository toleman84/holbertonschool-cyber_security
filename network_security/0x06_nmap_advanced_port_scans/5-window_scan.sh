#!/bin/bash
sudo nmap -PA $1 -p $2 -exclude-ports $3
