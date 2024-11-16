#!/usr/bin/python3

"""
Usage: read_write_heap.py pid search_string replace_string
where pid is the pid of the running process
and strings are ASCII

Output: you can print whatever you think is interesting

On usage error, print an error message on stdout and exit with status code 1
"""

def find_heaps(pid):
    """ find the heap address range in the progress """