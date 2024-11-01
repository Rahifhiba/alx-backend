#!/usr/bin/python3
""" FIFO CACHING"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching"""

    def put(self, key, item):
        """Add an item in the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data.values()) > BaseCaching.MAX_ITEMS:
                tmp = list(self.cache_data)[0]
                self.cache_data.pop(tmp)
                print("DISCARD: {}".format(tmp))

    def get(self, key):
        """Get an item by key"""
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
