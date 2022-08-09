def printNames(i,n):
    if i>n:
        return
    print("Anurag")    
    printNames(i+1,n)
N=int(input()) 
printNames(1,N)       