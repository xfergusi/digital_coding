import argparse
from unittest.mock import patch, MagicMock
from src.main import setup, get_ip_from_log, get_url_from_log, main

def test_get_ip_from_log():
    log = "192.168.1.1 - - [10/Oct/2000:13:55:36 -0700] \"GET /apache_pb.gif HTTP/1.0\" 200 2326"
    assert get_ip_from_log(log) == "192.168.1.1"

def test_get_url_from_log():
    log = "192.168.1.1 - - [10/Oct/2000:13:55:36 -0700] \"GET /apache_pb.gif HTTP/1.0\" 200 2326"
    assert get_url_from_log(log) == "/apache_pb.gif"

@patch('argparse.ArgumentParser.parse_args')
def test_setup(mock_parse_args):
    mock_parse_args.return_value = argparse.Namespace(log_file='test.log')
    args = setup()
    assert args.log_file == 'test.log'
    @patch('src.main.get_logs_into_memory')
    @patch('src.main.StatsTracker')
    @patch('argparse.ArgumentParser.parse_args')
    def test_main(mock_parse_args, mock_stats_tracker, mock_get_logs_into_memory):
        # Mock the command-line arguments
        mock_parse_args.return_value = argparse.Namespace(log_file='test.log')

        # Mock the logs returned by get_logs_into_memory
        mock_get_logs_into_memory.return_value = [
            "192.168.1.1 - - [10/Oct/2000:13:55:36 -0700] \"GET /apache_pb.gif HTTP/1.0\" 200 2326",
            "192.168.1.2 - - [10/Oct/2000:13:56:36 -0700] \"GET /index.html HTTP/1.0\" 200 1234"
        ]

        # Mock the StatsTracker methods
        mock_stats_tracker_instance = MagicMock()
        mock_stats_tracker.return_value = mock_stats_tracker_instance

        # Call the main function
        main()

        # Assert that get_logs_into_memory was called with the correct argument
        mock_get_logs_into_memory.assert_called_once_with('test.log')

        # Assert that StatsTracker methods were called with the correct arguments
        mock_stats_tracker_instance.unique_ip_addresses_input.assert_any_call("192.168.1.1")
        mock_stats_tracker_instance.unique_ip_addresses_input.assert_any_call("192.168.1.2")
        mock_stats_tracker_instance.most_active_ip_addresses_input.assert_any_call("192.168.1.1")
        mock_stats_tracker_instance.most_active_ip_addresses_input.assert_any_call("192.168.1.2")
        mock_stats_tracker_instance.most_visited_urls_input.assert_any_call("/apache_pb.gif")
        mock_stats_tracker_instance.most_visited_urls_input.assert_any_call("/index.html")

        # Assert that the analysis methods were called
        mock_stats_tracker_instance.unique_ip_addresses_analyse.assert_called_once()
        mock_stats_tracker_instance.most_visited_urls_analyse.assert_called_once()
        mock_stats_tracker_instance.most_active_ip_addresses_analyse.assert_called_once()
