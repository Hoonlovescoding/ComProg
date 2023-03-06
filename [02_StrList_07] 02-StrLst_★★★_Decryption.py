i = input()
a = i[3::7]
b = i[7::5]
c = int(a)+int(b)+10000
cc = str(c)[-4:-1]
d = int(cc[0])+int(cc[1])+int(cc[2]) #%10 ก้ได้หลักหน่วย
e = int(str(d)[-1])+1
alpha = ["A","B","C","D","E","F","G","H","I","J"]
f = alpha[e-1]
g = str(cc)+f
print(g)