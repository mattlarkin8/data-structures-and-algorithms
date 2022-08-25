def quick_sort(nums, left, right):
    if left < right:
        position = partition(nums, left, right)
        quick_sort(nums, left, position - 1)
        quick_sort(nums, position + 1, right)

    return nums

def partition(nums, left, right):
    pi = left
    pivot = nums[right]

    while nums[pi] <= pivot:
        pi += 1

    i = pi
    while nums[i] > pivot:
        i += 1

    swap(nums, i, pi)

    return pi

def swap(nums, i, pi):
    if i != pi:
        nums[i], nums[pi] = nums[pi], nums[i]


if __name__ == '__main__':
    test = [5,12,7,5,5,7]
    print(quick_sort(test, 0, 5))
