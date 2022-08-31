from data_structures.hashtable import Hashtable

def left_join(hash_a, hash_b):
    hash_a_keys = hash_a.keys()
    joined = []

    for key in hash_a_keys:
        item = [key, hash_a.get(key)]
        right = hash_b.get(key)
        if right is None:
            item.append("NONE")
        else:
            item.append(right)
        joined.append(item)

    return joined
