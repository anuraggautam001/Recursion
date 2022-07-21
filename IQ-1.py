def SumDigits(n):
    assert n>=0 and int(n)==n, 'The number has to be a positive integer only'

    if n==0:
        return 0
    else:
        return int(n%10) + SumDigits(int(n//10))

print(SumDigits(56656565))            
    
    