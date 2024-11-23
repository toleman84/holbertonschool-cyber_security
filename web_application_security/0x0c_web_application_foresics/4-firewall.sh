#!/bin/bash
grep "iptables -A INPUT" auth.log | wc -l
