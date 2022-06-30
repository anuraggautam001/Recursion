def fibo(a):
    assert a>=0 and int(a)==a, 'Fibonacci numbers can not be negative numbers or non integers.'
    if a in [0,1]:
        return a
    else:
        return fibo(a-1)+fibo(a-2)

n=int(input("Enter the place of fibonacci series: "))
print(fibo(n))
