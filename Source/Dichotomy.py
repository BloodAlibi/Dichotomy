# BloodAlibi // 2023

def dichotomy(lst, value):
    """
    Returns if a value is in a sorted list of numbers, and its index.
    /!\ ONLY TAKES SORTED LISTS!!
    """
    left=0
    right=len(lst)-1
    while right>=left:
        middle=((left+right)//2)
        if lst[middle] == value:
            return True, middle # Returns the value index and True
        else:
            if value > lst[middle]:
                left=middle+1
            else:
                right=middle-1
    return False, None # Returns False, and None
