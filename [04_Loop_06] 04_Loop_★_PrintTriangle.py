h = int(input())
w = (2*h)-1

print(' '*(h-1)+'*')

for i in range(h-2):
    print(' '*(h-2-i)+'*'+' '*(2*i+1)+'*')

print('*'*(2*h-1))
