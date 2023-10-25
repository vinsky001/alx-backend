#!/usr/bin/env python3
"""
Least Frequently Used (LFU) cache
"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """LFU cache class"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.keys = {}

    def put(self, key, item):
        """Add an item in the cache"""
        if key is not None and item is not None:
            if key in self.keys:
                self.keys[key] += 1
            else:
                self.keys[key] = 1
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    discard = min(self.keys, key=self.keys.get)
                    print("DISCARD: {}".format(discard))
                    self.keys.pop(discard)
                    self.cache_data.pop(discard)
                self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        self.keys[key] += 1
        return self.cache_data[key]
