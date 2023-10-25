#!/usr/bin/env python3
"""
Most Recently Used Cache
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class
    """

    def __init__(self):
        """
        Init
        """
        super().__init__()
        self.mru = []

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.mru.remove(key)
        self.cache_data[key] = item
        self.mru.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last = self.mru.pop(-2)
            print("DISCARD: {}".format(last))
            del self.cache_data[last]

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        self.mru.remove(key)
        self.mru.append(key)
        return self.cache_data[key]
