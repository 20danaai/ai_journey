def duplicate_count(text):
    text=text.lower()
    distinct=set(text)
    count=0
    for char in distinct:
        if text.count(char)>1:
            count+=1
    return countCount
