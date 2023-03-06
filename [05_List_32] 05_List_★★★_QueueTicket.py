time = []
que = 0
nx = 0
quenum = []
ordercount = 0
xtime = []
sumtime = 0
n = int(input())
for k in range(n):
    c = input().split()
    if c[0] == 'reset':
        que += int(c[1])
    elif c[0] == 'new':
        quenum.append(que)
        print('ticket '+str(que))
        que += 1
        time.append(c[1])
    elif c[0] == 'next':
        print('call '+str(quenum[nx]))
        nx += 1
    elif c[0] == 'order':
        xtime.append(int(c[1])-int(time[nx-1]))
        print('qtime '+str(quenum[nx-1])+' '+str(xtime[ordercount]))
        ordercount += 1
        sumtime = xtime[-1]+sumtime
    elif c[0] == 'avg_qtime':
        avg = sumtime/ordercount
        print('avg_qtime '+str(round(avg,4)))