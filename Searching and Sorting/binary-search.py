def binary_search(nums, target):
    """
    Space complexity: O(1)
    """
    first = 0
    last = len(nums)-1

    while first <= last:
        midpoint = (first + last)//2
        #The next step is to evaluate if the value at the target position is the value we are looking for
        if nums[midpoint] == target:
            return midpoint
        #if the value at the midpoint is lower than the target, we don't care about the values lower.So we redefine first 
        elif nums[midpoint] < target:
            first = midpoint + 1 
        else: #if the value at the midpoint is greater than the target, we define the last to point at the value below the midpoint
            last = midpoint - 1 
    
    return None #if the target is not in nums.

    

def verify(index):
    if index is not None:
        print("target found at index:", index)
    else:
        print("Target not found in the list.")

numbers = [1,2,3,4,8]
# The values must be sorted! otherwise the algorithm might return None
output = binary_search(numbers, 10)
verify(output)
