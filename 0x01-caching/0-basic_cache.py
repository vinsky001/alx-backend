#!/usr/bin/env python3
"""Basic cache module"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Basic cache class"""

    def put(self, key, item):
        """ädd item to the cache system"""
        if key and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is not None:
            return self.cache_data.get(key)
        return None

    if __name__ == '__main__':
        my_cache = BasicCache()
        my_cache.print_cache()
        my_cache.put("A", "Hello")
        my_cache.put("B", "World")
        my_cache.put("C", "Holberton")
        my_cache.print_cache()
        print(my_cache.get("A"))
        print(my_cache.get("B"))
        print(my_cache.get("C"))
        print(my_cache.get("D"))
        my_cache.print_cache()
        my_cache.put("D", "School")
        my_cache.put("E", "Battery")
        my_cache.put("A", "Street")
        my_cache.print_cache()
        print(my_cache.get("A"))
