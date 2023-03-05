a = input().split()
b = []
for i in range(len(a)):
    b.append(int(a[i],2))
sum = b[0]+b[1]
print((bin(sum))[2:])