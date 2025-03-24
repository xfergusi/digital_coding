"""
Reads a log file and loads its non-empty, stripped lines into memory as a list of strings.

Further improvements:
- Add error handling for file reading
"""
def get_logs_into_memory(log_file: str) -> list:
    # Open the log file in read mode
    # Filter out empty lines and strip whitespace from each line
    with open(log_file, "r") as file:
        return list(map(str.strip, filter(str.strip, file)))
