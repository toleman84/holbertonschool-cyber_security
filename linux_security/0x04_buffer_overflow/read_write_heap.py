#!/usr/bin/python3
import sys


"""
Usage: read_write_heap.py pid search_string replace_string
where pid is the pid of the running process
and strings are ASCII

Output: you can print whatever you think is interesting

On usage error, print an error message on stdout and exit with status code 1
"""

def find_heap(pid):
    """ find the heap address range in the progress """
    maps_path = f"/proc/{pid}/maps"
    print("find heap function:")
    try:
        with open(maps_path, 'r') as file:
            for line in file:
                if 'heap' in line:
                    print(f"line: {line}")
                    start, end = line.split(' ')[0].split('-')
                    print(f"A LINE: {start}, {end}")
                    return int(start, 16), int(end, 16)
    except FileNotFoundError:
        print(f"Error: Process with pid {pid} not found")
        sys.exit(1)
    print(f"Error: No heap found")
    sys.exit(1)

def read_memory(pid, start, end):
    """Reads memory from the specified address range"""
    mem_path = f"proc/{pid}/mem"
    try:
        with open(mem_path, 'rb') as file:
            file.seek(start)
            print("read function:")
            print(f"file: {file}")
            return file.read(end - start)
    except PermissionError:
        print(f"Error: Permission denied while reading memory for process {pid}")
        sys.exit(1)

def write_memory(pid, start, data):
    """writes data to the specified memoy address range"""
    mem_path = f"/proc/{pid}/mem)"
    try:
        with open(mem_path, 'r+b') as file:
            file.seek(start)
            file.write(data)
    except PermissionError:
        print(f"Error: Permission denied while reading memory for process {pid}")
        sys.exit(1)

def replace_string_in_heap(pid, search_string, replace_string):
    """Searches for a string in the heap and replaces it"""
    print(f"strings: {search_string}, {replace_string}")
    search_bytes = search_string.encode('ascii')
    replace_bytes = replace_string.encode('ascii')
    print(f"bytes: {search_bytes}, {replace_bytes}")

    # find the heap's address range
    start, end = find_heap(pid)
    # read the heap memory
    heap_data = read_memory(pid, start, end)
    # search for the string in the heap
    index = heap_data.find(search_bytes)
    print(f"index: {index}")

    print(f"found '{search_string}' at address {hex(start + index)}")

    # replace the string in memory
    new_data = heap_data[:index] + replace_bytes + heap_data[index + len(search_bytes):]
    write_memory(pid, start + index, new_data[index:])
    print(f"replaced '{search_string}' with '{replace_string}' int he heap")

def main():
    """main function"""
    pid = sys.argv[1]
    search_string = sys.argv[2]
    replace_string = sys.argv[3]

    replace_string_in_heap(pid, search_string, replace_string)
    print(f"main function process number: {pid}")

if __name__ == "__main__":
    main()
