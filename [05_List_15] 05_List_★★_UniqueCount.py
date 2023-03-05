a = list(map(int, input().split()))
a.sort()
ans = []

for b in range(len(a)):
    #if a[b] not in ans: (timeout bcuz it checks the whole list)
    if a[b-1] != a[b]:
        ans.append(a[b])

print(len(ans))

if len(ans) > 10:
    print(ans[:10])
else:
    print(ans)