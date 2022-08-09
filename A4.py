def backPrint(i,n):
    if(i<1):
        return
    backPrint(i-1,n)
    print(i)

N=int(input())
backPrint(N,N)        