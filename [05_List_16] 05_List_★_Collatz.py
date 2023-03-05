n = int(input())
ans = []
ans.append(str(n))

while n != 1:
    if n%2 == 0:
        n = round(n/2, 0)
    else:
        n = 3*n+1
    ans.append(str(int(n)))
    
if len(ans) > 15:
    p = '->'.join(ans[-15:])
    print(p)
else:
    p = '->'.join(ans)
    print(p)