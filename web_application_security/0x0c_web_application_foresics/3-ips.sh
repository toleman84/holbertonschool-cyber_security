#!/bin/bash
grep "Accepted password for root" auth.log | awk '{print $(NF-3)}' | sort | uniq -c | sort -nr | wc -l
