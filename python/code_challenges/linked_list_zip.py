from python.data_structures.linked_list import LinkedList
Linked = LinkedList

def zip_lists(a, b):
    idx_count = 0
    if Linked.get_length(a) > Linked.get_length(b):
        length = Linked.get_length(a)
    else:
        length = Linked.get_length(b)

    while idx_count < length:
        zipped_list = LinkedList()
        list1 = a.head
        list2 = b.head

        turn = 1
        if list1 is None:
            turn = 2
        if list2 is None:
            turn = 1

        while list1:
            if turn == 1:
                zipped_list.append(list1.value)
                list1 = list1.next
                turn = 2

        while list2:
            if turn == 2:
                zipped_list.append(list2.value)
                list2 = list2.next
                turn = 1

        idx_count += 1
