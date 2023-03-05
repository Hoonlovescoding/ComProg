ids = []
grades = []
uids = []
sgrade = ['A','B+','B','C+','C','D+','D','F']
ans = ''

while True:
    a = input().split()
    if a[0] == 'q':
        break
    ids.append(a[0])
    grades.append(a[1])

uids = input().split()
newids = sorted(ids)
newgrades = []
for i in newids:
    pos = ids.index(i)
    newgrades.append(grades[pos])

for i in newids:   
    if i in uids:
        c = newgrades[newids.index(i)]
        ans = i+' '
        if c != 'A':
            d = sgrade.index(c)
            ans += sgrade[d-1]
        else:
            ans += c
        print(ans)
    else:
        print(i+' '+newgrades[newids.index(i)])