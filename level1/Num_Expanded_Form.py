def expanded_form(num):
    str_num=str(num)
    result=[]
    lenght=len(str_num)
    for i in range(lenght):
        if str_num[i]!="0":
            zeros="0"*(lenght-i-1)
            result.append(str_num[i]+zeros)
    return " + ".join(result)
