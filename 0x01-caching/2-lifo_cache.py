#!/usr/bin/env python3
"""
Last In First Out (LIFO) cache
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO cache class """

    def __init__(self):
        """ Initiliaze """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            if key in self.keys:
                self.keys.remove(key)
            self.keys.append(key)
            self.cache_data[key] = item
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                last = self.keys.pop(-2)
                print("DISCARD: {}".format(last))
                del self.cache_data[last]

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
