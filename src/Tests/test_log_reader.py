import pytest
import os

from log_reader import get_logs_into_memory

def test_get_logs_into_memory():
    log_file = "src/Tests/test_logs/test_log_file.txt"
    with open(log_file, "w") as f:
        f.write("log1\nlog2\nlog3\n")

    logs = get_logs_into_memory(log_file)
    assert logs == ["log1", "log2", "log3"]

def test_get_logs_into_memory_empty_file():
    log_file = "src/Tests/test_logs/test_empty_log_file.txt"
    with open(log_file, "w") as f:
        f.write("")

    logs = get_logs_into_memory(log_file)
    assert logs == []

def test_get_logs_into_memory_with_whitespace():
    log_file = "src/Tests/test_logs/test_whitespace_log_file.txt"
    with open(log_file, "w") as f:
        f.write("log1\n\nlog2\n  \nlog3\n")

    logs = get_logs_into_memory(log_file)
    print(logs)
    assert logs == ["log1", "log2", "log3"]

# @pytest.fixture(scope="function", autouse=True)
# def cleanup():
#     os.remove("src/Tests/test_logs/test_whitespace_log_file.txt") 
#     os.remove("src/Tests/test_logs/test_empty_log_file.txt")
#     os.remove("src/Tests/test_logs/test_log_file.txt")