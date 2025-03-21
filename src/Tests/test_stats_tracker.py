import pytest
from src.stats_tracker import StatsTracker


@pytest.fixture
def stats_tracker():
    return StatsTracker()


def test_unique_ip_addresses_input(stats_tracker):
    stats_tracker.unique_ip_addresses_input("192.168.1.1")
    stats_tracker.unique_ip_addresses_input("192.168.1.2")
    stats_tracker.unique_ip_addresses_input("192.168.1.1")  # Duplicate IP
    assert stats_tracker.unique_ip_addresses_analyse() == 2


def test_most_visited_urls_input(stats_tracker):
    stats_tracker.most_visited_urls_input("http://example.com")
    stats_tracker.most_visited_urls_input("http://example.com")
    stats_tracker.most_visited_urls_input("http://example.org")
    top_three = stats_tracker.most_visited_urls_analyse()
    assert top_three == [("http://example.com", 2), ("http://example.org", 1)]


def test_most_active_ip_addresses_input(stats_tracker):
    stats_tracker.most_active_ip_addresses_input("192.168.1.1")
    stats_tracker.most_active_ip_addresses_input("192.168.1.1")
    stats_tracker.most_active_ip_addresses_input("192.168.1.2")
    top_three = stats_tracker.most_active_ip_addresses_analyse()
    assert top_three == [("192.168.1.1", 2), ("192.168.1.2", 1)]
