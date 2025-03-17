from stats_tracker_utils import *

class StatsTracker:
    unique_IP_addresses = set()

    def unique_ip_addresses_input(self, ip_address):
        self.unique_IP_addresses.add(ip_address)
    
    def unique_ip_addresses_analyse(self):
        return len(self.unique_IP_addresses)

    most_visited_urls = dict()

    def most_visited_urls_input(self, url):
        # take the string url, and add it the dictionary most_visited_urls, with the current value +1
        most_active_log_add_input(self.most_visited_urls, url)
    
    def most_visited_urls_analyse(self):
        # find the top three values of the and their urls from most_visited_urls
        return most_active_log_analyse_top_three(self.most_visited_urls)
    
    most_active_ip_addresses = dict()

    def most_active_ip_addresses_input(self, ip_address):
        # take the string url, and add it the dictionary most_visited_urls, with the current value +1
        most_active_log_add_input(self.most_active_ip_addresses, ip_address)

    def most_active_ip_addresses_analyse(self):
        # find the top three values of the and their urls from most_visited_urls
        return most_active_log_analyse_top_three(self.most_active_ip_addresses)