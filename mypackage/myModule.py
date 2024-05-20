def top_n (items, n):
    """Return the top n items in an array, in desc order.
    
    Args:
        items (array): an array or list like object
        n (int): the num of items to return
    
    Return:
        array: top n items in desc order

    Egs:
        >>> top_n ([8, 4, 3, 2, 7], 3)
        [8, 7, 4]
    """

    for i in range(n): # keep sorting until we have the top n items
        for j in range(len(itedms-1-i)):

            if item[j] > item[j+1]: # if this item is bigger than the next itme..
                item[j], item[j+1] = item[j+1], item[j] # swap the two!


    # get the last n items
    top_n = items[-n:]

    # return in desc oreder
    return top_n[::-1]