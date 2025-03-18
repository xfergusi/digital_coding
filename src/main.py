import argparse
from stats_tracker import StatsTracker
from log_reader import get_logs_into_memory

def setup():
    parser = argparse.ArgumentParser(description="Input for log analyser")
    parser.add_argument("--log_file", type=str, required=True, help="provide a log file you wish to analyse")
    return parser.parse_args()

def get_ip_from_log(log):
    return log.split(" ")[0]

def get_url_from_log(log):
    return log.split(" ")[6]

def print_stats(stats_tracker):

    print()
    print("The number of unique IP addresses")
    print(stats_tracker.unique_ip_addresses_analyse())
    print()
    print("The top 3 most visited URLs")
    print(stats_tracker.most_visited_urls_analyse())
    print()
    print("The top 3 most active IP addresses")
    print(stats_tracker.most_active_ip_addresses_analyse())
    print()

def gather_stats_from_logs(logs_list, stats_tracker):
    for log in logs_list:
        ip_address = get_ip_from_log(log)
        stats_tracker.unique_ip_addresses_input(ip_address)
        stats_tracker.most_active_ip_addresses_input(ip_address)

        url = get_url_from_log(log)
        stats_tracker.most_visited_urls_input(url)

def main():
    # take in command line arguments
    args = setup()

    # read the logs into memory and store them in a list by line
    logs_list = get_logs_into_memory(args.log_file)

    # create a new instance of the object that will keep track of statistics
    stats_tracker = StatsTracker()

    # loop through the logs list and gather statistics
    gather_stats_from_logs(logs_list, stats_tracker)

    # print the statistics we care about
    print_stats(stats_tracker)

if __name__ == "__main__":
    main()