n = int(input())
all = []
s1 = []

for i in range(n):
    a = int(input())
    s1.append(a)

s2 = input().split()
if s2 != -1:
    for b in range(len(s2)):
        s1.append(int(s2[b]))
    while True:
        c = int(input())
        if c == -1:
            break
        else:
            s1.append(c)

for d in range(len(s1)):
    if d%2 == 0:
        all.append(s1[d])
    else:
        all.insert(0, s1[d])

print(all)