#!/usr/bin/env python3
"""Basic cache module"""

from base_caching import Basecaching


class BaseCache(BaseCaching):
    """Basic cache class"""

    def put(self, key, item):
        """ädd item to the cache system"""
        if key and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is not None:
            return self.cache_data(key)
        return None
