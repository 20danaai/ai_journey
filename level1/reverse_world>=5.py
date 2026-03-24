  def spin_words(sentence):
    word=sentence.split()
    result=[]
    for i in word:
        if len(i)>=5:
            result.append(i[::-1])
        else:
            result.append(i)
    return" ".join(result)
