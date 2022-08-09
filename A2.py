def printNum(i,n):
    if(i>n):
        return
    print(i)
    printNum(i+1,n)


N = int(input())
printNum(1,N)