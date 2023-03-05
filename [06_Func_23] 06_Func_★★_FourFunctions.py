def make_int_list(x):
    list = [int(e) for e in x.split()]
    return list

def is_odd(e):
    if e%2 == 0:
        return False
    else:
        return True
    
def odd_list(alist):
    olist = []
    for i in range(len(alist)):
        if is_odd(alist[i]) is True:
            olist.append(alist[i])
    return olist

def sum_square(alist):
    total = 0
    for i in range(len(alist)):
        total += (alist[i]**2)
    return total

exec(input().strip())