#Problem:Convert sting to camel case
#Source:cdewars_kyu6
# Note:Split text and capitalize each word except the first one
def to_camel_case(text):
    text=text.replace("-","_")
    word=text.split("_")
    result=word[0]
    for i in word[1:]:
        result+=i.capitalize()
    return result
