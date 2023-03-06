i = input().split()
com = input()
n = len(i)
for a in com:
    if a == "C":
        i = i[n//2:] + i[:n//2]
    elif a == "S":
        s = [' ']*n
        s[::2] = i[:n//2]
        s[1::2] = i[n//2:]
        i = s
print(' '.join(i))

#use // bcuz / will get .0 at the end