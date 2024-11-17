#!/usr/bin/python3
import sys

"""
Script to read and modify strings in the heap section of an active process

Requirements:
    - script must be run with superuser privileges to access /proc/{pid}/mem
"""


def find_heap(pid):
    """
    Find the heap address range of a given process.

    Args:
        pid (int): process ID.

    Returns:
        tuple: Pair of int representing the start, end addresses of the heap

    Raises:
        FileNotFoundError: If the maps file is not found for the given process
        SystemExit: If the heap is not found in the maps.
    """
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
    """
    Reads a specific memory range from the given process.

    Args:
        pid (int): The process ID whose memory space is to be read.
        start (int): The starting address of the memory range to read.
        end (int): The ending address of the memory range to read.

    Returns:
        bytes: The data read from the specified memory range.

    Raises:
        PermissionError: If the script lacks perms to access the process's mem
        SystemExit: Terminates the program if an error occurs while access mem

    Details:
        - The file `/proc/<pid>/mem` provides access to the process mem space
        - The script must be run with superuser privileges to access this file
        - The function calculates the read range as `end - start` and uses
        `file.seek()` to position itself at the starting address.

    Example:
        >>> read_memory(1234, 0x7ff123400000, 0x7ff123500000)
        b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR...'

    Notes:
        - Ensure that `start` and `end` are within the heap range of the procs
        - If permissions are denied, run the script with superuser privileges
          (e.g., using `sudo`).
    """
    mem_path = f"/proc/{pid}/mem"
    try:
        with open(mem_path, 'r+b') as file:
            file.seek(start)
            print("read function:")
            print(f"file: {file}")
            return file.read(end - start)
    except PermissionError:
        print(f"Error: Permission denied while reading mem for process {pid}")
        sys.exit(1)


def write_memory(pid, start, data):
    """
    Writes data to a specific memory address range of a given process.

    Args:
        pid (int): The process ID whose memory space is to be modified.
        start (int): The starting address in the memory range where the
        data will be written.
        data (bytes): The data to be written into the specified memory range.

    Raises:
        PermissionError: If the script lacks the necessary permissions
        to access the process's memory file.
        SystemExit: Terminates the program if an error occurs during the memory
        write operation.

    Details:
        - The function accesses the `/proc/<pid>/mem` file to modify the memory
        of the process.
        - Superuser privileges are required to write to this file.
        - The `file.seek()` method is used to move to the specified starting
        address before writing the data.

    Example:
        >>> write_memory(1234, 0x7ff123400000, b'HelloWorld')
        This writes the string "HelloWorld" as bytes into the process memory
        starting at the given address.

    Notes:
        - The `data` must not exceed the available writable memory range
        starting from `start`.
        - Ensure the memory range being modified is safe to access and won’t
        cause unexpected behavior in the process.
        - If permissions are denied, run the script with superuser privileges
        (e.g., using `sudo`).
    """
    mem_path = f"/proc/{pid}/mem"
    try:
        with open(mem_path, 'r+b') as file:
            file.seek(start)
            file.write(data)
    except PermissionError:
        print(f"Error: Permission denied while reading mem for process {pid}")
        sys.exit(1)


def replace_string_in_heap(pid, search_string, replace_string):
    """
    Searches for a specific string in the heap of a process and replaces it
    with another string.

    Args:
        pid (int): The process ID of the target process whose heap memory will
        be modified.
        search_string (str): The string to search for in the heap.
        replace_string (str): The string that will replace the `search_string`
        in the heap.

    Raises:
        ValueError: If the `replace_string` is longer than the `search_string`.
        PermissionError: If the script lacks the necessary permissions to
        access  the process's memory.
        SystemExit: Terminates the program if an error occurs during the
        replacement process.

    Details:
        - This function searches for the `search_string` in the heap memory of
        the specified process and replaces it with the `replace_string`.
        - The heap memory is accessed via the `/proc/<pid>/mem` interface.
        - The function ensures that the `replace_string` is not longer than
        the `search_string` to prevent memory overflows.
        - It uses the `find_heap()` function to get the heap's memory address
        range and then reads the heap data to locate the `search_string`.

    Example:
        >>> replace_string_in_heap(1234, "old_string", "new_string")
        This replaces occurrences of the string "old_string" with "new_string"
        in the heap of the process with PID 1234.

    Notes:
        - The script must be run with superuser privileges (e.g., using `sudo`)
        to access the memory of other processes.
        - Ensure that the process is running and accessible via
        `/proc/{pid}/mem` before using this function.
        - If the `replace_string` is longer than the `search_string`, the
        function will terminate with an error.
    """
    print(f"strings: {search_string}, {replace_string}")
    search_bytes = search_string.encode('ascii')
    replace_bytes = replace_string.encode('ascii')
    print(f"bytes: {search_bytes}, {replace_bytes}")

    if len(replace_bytes) > len(search_bytes):
        print("Error: replace string is too longer than search string")
        sys.exit(1)

    # find the heap's address range
    start, end = find_heap(pid)
    # read the heap memory
    heap_d = read_memory(pid, start, end)
    # search for the string in the heap
    inx = heap_d.find(search_bytes)
    print(f"index: {inx}")
    if inx == -1:
        print(f"Error: string: '{search_string}' not found in a heap")
        sys.exit(1)

    print(f"found '{search_string}' at address {hex(start + inx)}")

    # replace the string in memory
    new_data = heap_d[:inx] + replace_bytes + heap_d[inx + len(search_bytes):]
    write_memory(pid, start + inx, new_data[inx:])
    print(f"replaced '{search_string}' with '{replace_string}' int he heap")


def main():
    """
    Args:
        None: This function only interacts with the command-line arguments.

    Raises:
        SystemExit: Terminates the program with status code 1 if the number of
        arguments is incorrect,
                    or if either `search_string` or `replace_string` contains
                    non-ASCII characters.

    Example:
        >>> python3 read_write_heap.py 1234 "old_string" "new_string"
        Replaces occurrences of "old_string" with "new_string" in the heap of
        the process with PID 1234.

    Notes:
        - The script must be run with appropriate permissions (e.g., `sudo`) to
        access the memory of other processes.
        - This function relies on the `replace_string_in_heap()` function to
        carry out the memory modification.

    """
    if len(sys.argv) != 4:
        print("Usage: read_write_heap.py pid search_string replace_string")
        sys.exit(1)

    pid = sys.argv[1]
    search_string = sys.argv[2]
    replace_string = sys.argv[3]

    if not search_string.isascii() or not replace_string.isascii():
        print("Error: Both search_string and replace_string must be ASCII.")
        sys.exit(1)

    replace_string_in_heap(pid, search_string, replace_string)
    print(f"main function process number: {pid}")


if __name__ == "__main__":
    main()
