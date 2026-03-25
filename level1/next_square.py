import math
def find_next_square(sq):
    root=math.sqrt(sq)
    if root%1==0:
        next_root=root+1
        return next_root**2
    else:
        return -1
