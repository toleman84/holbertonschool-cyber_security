#!/bin/bash
find "$1" -tyep f -user user2 -exec chown user3 {} \;
