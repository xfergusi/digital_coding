def get_logs_into_memory(log_file):
    with open(log_file, "r") as file:
        return list(map(str.strip, filter(str.strip, file)))
