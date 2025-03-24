"""
Extracts the URL from a log entry.

Further improvements:
- Add parameter validation
- Add variability in the log format
"""
def get_ip_from_log(log: str) -> str:
    return log.split(" ")[0]


def get_url_from_log(log: str) -> str:
    return log.split(" ")[6]
