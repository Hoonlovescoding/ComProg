full = ['Robert','William','James','John','Margaret','Edward','Sarah','Andrew','Anthony','Deborah']
nick = ['Dick','Bill','Jim','Jack','Peggy','Ed','Sally','Andy','Tony','Debbie']

i = int(input())
for a in range(i):
    n = input()
    if n in full:
        pos = full.index(n)
        print(nick[pos])
    elif n in nick:
        pos = nick.index(n)
        print(full[pos])
    else:
        print('Not found')