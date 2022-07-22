def DecToBin(n):
    assert int(n)==n,'The parameter must be an integer only'

    if n==0:
        return 0
    else:
        return n%2 + 10 * DecToBin(n//2)

print(DecToBin(10))            