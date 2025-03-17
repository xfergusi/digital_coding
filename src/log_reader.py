def get_logs_into_memory(log_file):
    # read in the file and bring all the logs into memory
    with open(log_file, "r") as f:
        logs = f.readlines()
    return [log.strip() for log in logs if log.strip()]