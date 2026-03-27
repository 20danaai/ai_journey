#problem:1)if num repeat three times ,it scores a large bonus.2) the num 1 and 5 provide extra points even if they do not appear as a triplet.
#source:cde_kyu5
def score(dice):
    total=0
    for i in range(1,7):#we pass through all elements 
        count=dice.count(i)#count how many times the num i appears
        if count>=3:#calculate the points if the num appears 3 or more times
            if i==1:total+=1000
            else:total+=i*100
            count-=3# remove the 3 dice that were already counted
          #calculate the remaining points (for individual 1s and 5s)
        if i ==1:
            total+=count*100
        elif i==5:
            total+=count*50
    return total
