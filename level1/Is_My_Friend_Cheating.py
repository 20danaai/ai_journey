#Problem:find (a,b) from a sequence 1 to n such that a*b equals the sum of all other numbers in the sequence.
#Source:cdewars_kyu5
#Note:removed (a,b) and their product (*) is equal to the sum of the remaining num in the sequence
def remov_nb(n):
    sum=n*(n+1)//2 # i use this not loop cause this faster (summing num manually)
    result=[]# storage
    for i in range(1,n+1):# n+1 for include n
        b=(sum-i)/(i+1)   #problem says a*b=sum -a-b look to the note you will understand ,a*b+b=sum-a,b(a+1)=sum-a,b=(sum-a)/a+1
        if b.is_integer()and b <=n and b!=i:
            result.append((i),int(b))) # include all the num
    return result
  
