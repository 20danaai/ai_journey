def solution(n):
    roman=[(1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),(100,'C'),(90,"XC"),(50,"L"),(40,"XL"),(10,"X"),(9,"IX"),(5,"V"),(4,"IV"),(1,"I")] #roman number - from each other
    result=""#storage
    for value, symbol in roman:#(value,"symbol")
        while n>=value:
                result+=symbol#+storage to reveal a string
                n-=value#to reach for less number
    return result
