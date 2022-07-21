def PowNum(n,p):
    assert p>=0 and int(p)==p,'The exponent must be a postive integer only!'
    if p==0:
        return 1
    if p==1:
        return n    
    return n * PowNum(n,p-1)


print(PowNum(-2,4))    