def find_uniq(arr):
    a,b=set(arr)
    if arr[:3].count(a)>=2:
        return b
    return a
