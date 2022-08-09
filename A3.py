def printNum(i,n):
    if(i<1):
        return
    print(i)
    printNum(i-1,n)

N = int(input())
printNum(N,N)        