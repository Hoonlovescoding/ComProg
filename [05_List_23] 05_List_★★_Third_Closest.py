r = int(input())
cords = []
for i in range(r):
    ocords = input().split()
    cords.append(float(ocords[0]))
    cords.append(float(ocords[1]))

dis = []
for i in range(int(len(cords)/2)):
    dis.append(((cords[2*i])**2+(cords[2*i+1])**2)**0.5)

ndis = sorted(dis)
third = dis.index(ndis[2])

print('#'+str(third+1)+': ('+str(cords[third*2])+', '+str(cords[2*third+1])+')')