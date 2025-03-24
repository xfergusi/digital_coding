import pytest
import os

from src.logfile_reader import get_logs_into_memory


@pytest.fixture(scope="function", autouse=True)
def cleanup():
    os.makedirs("src/Tests/test_logs/", exist_ok=True)


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
    assert logs == ["log1", "log2", "log3"]


def test_get_logs_into_memory():
    log_file = "src/Tests/test_logs/test_log_file.txt"
    with open(log_file, "w") as f:
        f.write("log1 asdf asdf asdf asdf asdf asdf   \nlog2\nlog3\n")

    logs = get_logs_into_memory(log_file)
    assert logs == ["log1 asdf asdf asdf asdf asdf asdf", "log2", "log3"]
