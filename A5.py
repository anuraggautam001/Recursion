def backPrint(i,n):
    if(i>n):
        return
    backPrint(i+1,n)
    print(i)

N = int(input())
backPrint(1,N)        