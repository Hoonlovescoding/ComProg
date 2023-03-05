#all = [0,1,2,3,4,5,6,7,8,9]

#i = input()
#a = range(len(all))

#if all.count(a) > 0:
#    all.remove(a)

#print(all)

all =[0,1,2,3,4,5,6,7,8,9]
all = list(map(str,all))
i = input()

for a in i:
    if a in all:
        all.remove(a)

if len(all) == 0:
    print('None')
else:
    print(",".join(all))