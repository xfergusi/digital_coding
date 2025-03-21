from stats_tracker_utils import most_active_log_add_input, most_active_log_analyse_top_three

"""
Module: stats_tracker

This module provides the `StatsTracker` class, which is used to track and analyze 
various statistics related to IP addresses and URLs. It supports tracking unique 
IP addresses, the most visited URLs, and the most active IP addresses.

Further improvements:
- Add currently we have no way of assessing "ties" in the top three most visited URLs or most active IP addresses.
"""
class StatsTracker:
    unique_ip_addresses = set()

    def unique_ip_addresses_input(self, ip_address):
        self.unique_ip_addresses.add(ip_address)

    def unique_ip_addresses_analyse(self):
        return len(self.unique_ip_addresses)

    most_visited_urls = dict()

    def most_visited_urls_input(self, url):
        # Add the string `url` to the dictionary `most_visited_urls` with the current value +1
        most_active_log_add_input(self.most_visited_urls, url)

    def most_visited_urls_analyse(self):
        # Find the top three values and their URLs from `most_visited_urls`
        return most_active_log_analyse_top_three(self.most_visited_urls)

    most_active_ip_addresses = dict()

    def most_active_ip_addresses_input(self, ip_address):
        # Add the string `ip_address` to the dictionary `most_active_ip_addresses` with the current value +1
        most_active_log_add_input(self.most_active_ip_addresses, ip_address)

    def most_active_ip_addresses_analyse(self):
        # Find the top three values and their IP addresses from `most_active_ip_addresses`
        return most_active_log_analyse_top_three(self.most_active_ip_addresses)
