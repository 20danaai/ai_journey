def to_camel_case(text):
    text=text.replace("-","_")
    word=text.split("_")
    result=word[0]
    for i in word[1:]:
        result+=i.capitalize()
    return result
