def Factorial(n):
    assert n>=0 and int(n) == n, 'The number must be positive integer only'   #assert keyword is used to test if a condition in your code is true, if not, it returns as assertionError
    if n in [0,1]:   #Base condition-- to stop the flow
        return 1
    else:
        return n*Factorial(n-1)     #recursive flow

x=int(input("Enter the number to find factorial "))
print(Factorial(x))            