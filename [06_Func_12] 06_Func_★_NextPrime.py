def is_prime(n):
    #Check if n is a prime number(provided on sheet)
    if n <= 1:
        return False
    for k in range(2, int(n**0.5)+1):
        if n%k == 0:
            return False
    return True

def next_prime(n):
    n+=1
    while is_prime(n) is False:
        n+=1
    return n

def next_twin_prime(n):
    a = next_prime(n)
    b = next_prime(a)
    while b-a != 2:
        a = next_prime(a)
        b = next_prime(a)
    return a,b

#this command is necessary to grade your answer(provided on sheet)
exec(input().strip())