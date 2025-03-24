import argparse
from stats_tracker import StatsTracker
from logfile_reader import get_logs_into_memory
from log_parser import get_ip_from_log, get_url_from_log
import traceback

def setup():
    parser = argparse.ArgumentParser(description="Input for log analyser")
    parser.add_argument(
        "--log_file",
        type=str,
        required=True,
        help="provide a log file you wish to analyse"
    )
    return parser.parse_args()


"""
Prints statistical analysis of logs using the provided stats_tracker.

Futher improvements:
- Add more statistical analysis
- Add parameters to only print certain statistics
- Make it prettier when printed. Right now I'm just printing the raw data.
"""
def print_stats(stats_tracker: StatsTracker):
    print(
        f"The number of unique IP addresses:\n"
        f"{stats_tracker.unique_ip_addresses_analyse()}"
    )
    print(
        f"The top 3 most visited URLs:\n"
        f"{stats_tracker.most_visited_urls_analyse()}"
    )
    print(
        f"The top 3 most active IP addresses:\n"
        f"{stats_tracker.most_active_ip_addresses_analyse()}"
    )


"""
Processes a list of log entries to gather statistics on IP addresses and URLs.

Further improvements:
- Add parameters to only perform analysis on certain statistics
- Improve error handling
"""
def gather_stats_from_logs(logs_list: list, stats_tracker: StatsTracker):
    try:
        for log in logs_list:
            ip_address = get_ip_from_log(log)
            stats_tracker.unique_ip_addresses_input(ip_address)
            stats_tracker.most_active_ip_addresses_input(ip_address)

            url = get_url_from_log(log)
            stats_tracker.most_visited_urls_input(url)
            exit()
    except Exception as e:
        print(f"Error gathering stats from logs, specific details below:")
        print(e)
        traceback.print_exc()
        exit(1)

def main():
    # take in command line arguments
    args = setup()

    # read the logs into memory and store them in a list by line
    # [line1, line2, line3, ...]
    logs_list = get_logs_into_memory(args.log_file)

    # create a new instance of the object that will keep track of statistics
    stats_tracker = StatsTracker()

    # loop through the logs list and gather statistics
    gather_stats_from_logs(logs_list, stats_tracker)

    # print the statistics we care about
    print_stats(stats_tracker)


if __name__ == "__main__":
    main()
