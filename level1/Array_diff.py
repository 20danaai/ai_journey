#this function requires removing all elements present in list b from list a while preserving the original order 
# level kyu6
def array_diff(a, b):
    set_b=set(b)
    return [i for i in a if i not in set_b]# not in use for list 
  # another way (not use set )
  # return[i for i in a if i not in b]
