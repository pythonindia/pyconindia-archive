def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) / 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(a1, a2):
    res = []
    while len(a1) > 0 and len(a2) > 0:
        if a1[0] < a2[0]:
            res.append(a1[0])
            a1.pop(0)
        else:
            res.append(a2[0])
            a2.pop(0)
    if len(a1) > 0:
        res.extend(a1)
    if len(a2) > 0:
        res.extend(a2)
    return res
