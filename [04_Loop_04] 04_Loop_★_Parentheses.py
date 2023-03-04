n = input()
a = ''
for b in n:
    if b == '(':
        a += '['
    elif b == '[':
        a += '('
    elif b == ')':
        a += ']'
    elif b == ']':
        a += ')'
    else:
        a += b
print(a)