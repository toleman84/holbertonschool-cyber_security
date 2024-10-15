#!/bin/bash
find / -xdev -type d -perm -0002 -print 2>/dev/null
