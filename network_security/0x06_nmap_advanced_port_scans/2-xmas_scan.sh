#!/bin/bash
sudo nmap -sX -p 440-450 --packet-trace $1
