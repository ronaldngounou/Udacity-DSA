def quicksort(nums):
    """
    Time complexity: O(n log n)
    Works by placing the elements less than the pivot on the left, and the elements greater than the pivot on the right
    """

    if len(nums) <= 1:
        return nums

    pivot = nums[0]
    less_than_pivot = []
    greater_than_pivot = []

    for num in nums[1:]:
        if num <= pivot:
            less_than_pivot.append(num)
        else:
            greater_than_pivot.append(num)

    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

numbers = [4,6,3,2,9,7,3,5]

print("Sorterd array:", quicksort(numbers))
