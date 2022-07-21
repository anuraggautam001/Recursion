def sumL(lst):
    if len(lst)==1:
        return lst[0]
    else:
        return lst[0]+sumL(lst[1:])

FL=[1,2,3,4]
print(sumL(FL))        