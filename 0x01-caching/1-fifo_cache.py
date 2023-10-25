#!/usr/bin/env python3
"""
First in First out cache replacement algorithm
"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching system"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ Add an item in the cache"""
        if key and item is not None:
            if key in self.keys:
                self.keys.remove(key)
            self.keys.append(key)
            self.cache_data[key] = item
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                discard = self.keys.pop(0)
                del self.cache_data[discard]
                print("DISCARD: {}".format(discard))

    def get(self, key):
        """Get an item by key"""
        if key is not None:
            return self.cache_data.get(key)
        return None
