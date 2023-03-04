#key = input()
#sent = input()

#num = sent.count(key)
#print(num)

key = input()
sent = input()
why = ''
for a in sent:
    if a in ['"','(',')',',','.',"'"]:
        why += ' '
    else:
        why += a
a = 0
for b in why.split():
    if b == key:
        a += 1
print(a)