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

for i in ids:   
    if i in uids:
        c = grades[ids.index(i)]
        ans = i+' '
        if c != 'A':
            d = sgrade.index(c)
            ans += sgrade[d-1]
        else:
            ans += c
        print(ans)
    else:
        print(i+' '+grades[ids.index(i)])