def mergesort(nums):
    """
    Time complexity: O(n log n)
    """
    if len(nums) <= 1:
        return nums
    else:
        mid = len(nums)//2
        left_values = mergesort(nums[:mid])
        right_values = mergesort(nums[mid:])
        left_idx = 0
        right_idx = 0 
        sorted_array = []

        while left_idx < len(left_values) and right_idx < len(right_values):
        
            if left_values[left_idx] < right_values[right_idx]:
                sorted_array.append(left_values[left_idx])
                left_idx += 1
            else:
                sorted_array.append(right_values[right_idx])
                right_idx += 1

        sorted_array += right_values[right_idx:]
        sorted_array += left_values[left_idx:]
    
    return sorted_array

numbers = [5,2,3,1]
print("Sorterd array:", mergesort(numbers))
