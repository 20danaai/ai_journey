def dig_pow(n, p):
    s=0#series
    for i,c in enumerate(str(n)):#i endex,c value 
        s+=pow(int(c),p+i)
    return s//n if s%n==0 else -1# k= s//n
