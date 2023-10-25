#!/usr/bin/env python3
"""
Least Recently Used (LRU) cache replacement algorithm
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU cache class"""

    def __init__(self):
        """Constructor"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Add an item in the cache"""
        if key and item:
            if key in self.cache_data:
                self.keys.remove(key)
            self.cache_data[key] = item
            self.keys.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last = self.keys.pop(0)
                print("DISCARD: {}".format(last))
                del self.cache_data[last]

    def get(self, key):
        """Get an item by key"""
        if key in self.cache_data:
            self.keys.remove(key)
            self.keys.append(key)
            return self.cache_data[key]
        return None
