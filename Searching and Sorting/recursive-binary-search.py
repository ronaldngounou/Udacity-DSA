def recursive_binary_search(list, target):
    """
    Using a recursive process for binary search.

    Space complexity: O(log n)
    """


    #if an empty list is passed in
    if len(list)==0:
        return False
    else:
        midpoint = len(list) // 2
    
    if list[midpoint] == target:
        return True
    else:
        if list[midpoint] < target:
            #using slice lists
            return recursive_binary_search(list[midpoint+1:], target)
        else:
            return recursive_binary_search(list[:midpoint-1], target)


def verify(index):
    print("target found at index:", index)


numbers = [1,2,3,4,5,6,7,8]
# The values must be sorted! otherwise the algorithm might return None
output = recursive_binary_search(numbers, 12)
verify(output)
