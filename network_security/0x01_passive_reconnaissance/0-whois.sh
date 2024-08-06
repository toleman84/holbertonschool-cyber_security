#!/bin/bash
sudo whois "$1" | awk '/(Registrant|Admin|Tech)/' > "$1".csv
