def gcd(x,y):
    assert int(x)==x and int(y)==y,'The number must be integer only'

    if x<0:
        x= -1*x
    if y<0:
        y= -1*y
    if y==0:
        return x
    else:
        return gcd(y,x%y)

print(gcd(35,21))            