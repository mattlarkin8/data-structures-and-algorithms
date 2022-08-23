def merge_sort(nums):
    n = len(nums)

    if n > 1:
        mid = n // 2
        left = nums[0:mid]
        right = nums[mid:n]

        merge_sort(left)
        merge_sort(right)

        merge(left, right, nums)

    return nums

def merge(left, right, nums):
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1

        k += 1

    if i == len(left):
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
    else:
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

    return nums
