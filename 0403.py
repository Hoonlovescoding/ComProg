sol = input()
ans = input()
if len(sol) != len(ans):
    print('Incomplete answer')
else:
    c=0
    for i in range(len(sol)):
        if ans[i] == sol[i]:
            c += 1
    print(c)