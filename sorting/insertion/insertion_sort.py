def insertion_sort(list_):
    for i, val in enumerate(list_):
        j = i - 1
        temp = list_[i]

        while j >= 0 and temp < list_[j]:
            list_[j + 1] = list_[j]
            j = j - 1

        list_[j + 1] = temp

    return list_
