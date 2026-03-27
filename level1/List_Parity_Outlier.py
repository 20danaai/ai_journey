#problem:find the outlier in the list of numbers
#source:cde_kyu6
#
def find_outlier(integers):
    evens=[i for i in integers if i %2==0]
    odd=[i for i in integers if i %2!=0]
    if len(evens)==1:# if the even list contains only one element,then it is the outlier.
        return evens[0]#endex 0 cause there no one else
    else:
        return odd[0]
      # another way 
      # return odd[0] if len[odd]<len[even] else even[0]
