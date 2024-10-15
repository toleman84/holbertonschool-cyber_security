#!/bin/bash
sshd -T | grep -eV /etc/ssh/sshd_config
