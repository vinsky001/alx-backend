#!/usr/bin/env python3
"""
First in First out cache replacement algorithm
"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching system"""

    def __init__(self):
        """Initialize"""
        super().__init__():
            self.keys = []

    def put(self, key, item):
        """ Add an item in the cache"""
        if key and item is None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find and remove the first item added (FIFO)
                first_key = next(iter(self.cache_data))
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}")
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is None:
            return self.cache_data.get(key)
        return None
