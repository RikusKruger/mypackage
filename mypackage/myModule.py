def top_n(items, n):
    """
    Return top n items in array,in desc order.

    Args:
        items (array): list or array-like object
        n (int): num of items to return

    Return:
        array: top n items, in desc order

    Egs:
        >>> top_n([8, 3, 7, 2, 4])
"""
    
    return sorted(items, key = lambda x: x[1], reverse = True)[:n]