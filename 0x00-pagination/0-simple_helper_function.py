#!/usr/bin/env python3
"""
Simple helper function
"""


def index_range(page, page_size):
    """
    return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.
    """
    # Calculate the offset and limit
    start_index = (page - 1) * page_size
    end_index = page * page_size

    return(start_index, end_index)

    if __name__ == '__main__':
        res = index_range(1, 7)
        print(type(res))
        print(res)

        res = index_range(page=3, page_size=15)
        print(type(res))
        print(res)
