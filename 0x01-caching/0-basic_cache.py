#!/usr/bin/python3
"""class BasicCache that inherits from BaseCaching and is a caching system"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ """

    def put(self, key, item):
        """Add an item in the cache"""
        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data.keys():
            return self.cache_data[key]
        return None