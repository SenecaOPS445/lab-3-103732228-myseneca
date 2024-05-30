#!/usr/bin/env python3

# Author ID: 103732228

import subprocess

def free_space():
    # Run the df command and capture the output
    result = subprocess.run("df -h | grep '/$' | awk '{print $4}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Decode the output to a UTF-8 string and strip newline characters
    free_space_str = result.stdout.decode('utf-8').strip()
    
    return free_space_str

# Example usage
if __name__ == "__main__":
    print(f"Free space on root directory: {free_space()}")