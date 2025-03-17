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

def main():
    args = setup()

    logs_list = get_logs_into_memory(args.log_file)

    # loop through logs and gather stats we care about
    stats_tracker = StatsTracker()
    # I'm looping through this 
    for log in logs_list:
        print(log)
        ip_address = get_ip_from_log(log)
        stats_tracker.unique_ip_addresses_input(ip_address)
        stats_tracker.most_active_ip_addresses_input(ip_address)

        url = get_url_from_log(log)
        stats_tracker.most_visited_urls_input(url)

    print()
    print("The number of unique IP addresses")
    print(stats_tracker.unique_IP_addresses_analyse())
    print()
    print("The top 3 most visited URLs")
    print(stats_tracker.most_visited_urls_analyse())
    print()
    print("The top 3 most active IP addresses")
    print(stats_tracker.most_active_ip_addresses_analyse())

if __name__ == "__main__":
    main()