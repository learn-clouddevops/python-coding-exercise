#Parse a line like 2024-01-15 10:23:45 ERROR Disk full into a dict with date, time, level, message.

# line ="2024-01-15 10:23:45 ERROR Disk full error . Please increase the disk"


import os

def iterate_on_file(filepath):
    """Generator: yields parsed log dicts one at a time"""
    try:
        if not os.path.isfile(filepath):
            print("File not found")
            return
        
        with open(filepath, "r") as file:
            for line in file:
                parts = line.split(maxsplit=3)
                
                # Skip malformed lines
                if len(parts) < 4:
                    continue
                
                data = {
                    "date": parts[0],
                    "time": parts[1],
                    "level": parts[2],
                    "message": parts[3].strip()  # Remove trailing newline
                }
                yield data
    
    except FileNotFoundError:
        print("No FILE EXIST")


filepath = os.path.join(os.path.dirname(__file__), "loglevel.log")

if __name__ == "__main__":
    logfile = iterate_on_file(filepath)
    
    for item in logfile:
        print(item)
