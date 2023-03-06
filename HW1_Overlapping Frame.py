#frames = [float(x) for x in input().split()]
frames = [1.0,4.0,1.5,2.0,2.0,5.0,2.5,2.0,4.0,5.5,1.5,3.5,6.0,4.5,1.5,2.0]

def giveCords(i):
    x,y,w,h = frames[(i-1)*4], frames[(i-1)*4+1], frames[(i-1)*4+2], frames[(i-1)*4+3]
    return x,y,w,h

def giveCenter(i):
    x,y,w,h = giveCords(i)
    x,y = x+(w/2), y-(h/2)
    return x,y

def giveDistance(f1,f2):
    xf1,yf1 = giveCenter(f1)
    xf2,yf2 = giveCenter(f2)
    x,y = (xf1-xf2),(yf1-yf2)
    d = abs((x**2+y**2)**(1/2))
    return d

def giveInter(f1,f2):
    xf1,yf1,wf1,hf1 = giveCords(f1)
    xf2,yf2,wf2,hf2 = giveCords(f2)
    xinter = max(0, min(xf1+wf1, xf2+wf2) - max(xf1, xf2))
    yinter = max(0, min(yf1, yf2) - max(yf1-hf1, yf2-hf2))
    area = xinter*yinter
    return area

def giveUnion(f1,f2):
    interarea = giveInter(f1,f2)
    xf1,yf1,wf1,hf1 = giveCords(f1)
    xf2,yf2,wf2,hf2 = giveCords(f2)
    areaf1 = wf1*hf1
    areaf2 = wf2*hf2
    unionarea = areaf1+areaf2-interarea
    return unionarea

def giveiou(f1,f2):
    interarea = giveInter(f1,f2)
    unionarea = giveUnion(f1,f2)
    ratio = interarea/unionarea
    return ratio

clist = [0]

while clist[-1] != ['end']:
    clist.append(input().split())
clist.pop(0)

for i in range(len(clist)):
    if clist[i][0] == 'center':
        print(giveCenter(int(clist[i][1])))
    elif clist[i][0] == 'distance':
        print(giveDistance(int(clist[i][1]),int(clist[i][2])))
    elif clist[i][0] == 'intersection':
        print(giveInter(int(clist[i][1]),int(clist[i][2])))
    elif clist[i][0] == 'union':
        print(giveUnion(int(clist[i][1]),int(clist[i][2])))
    elif clist[i][0] == 'iou':
        print(giveiou(int(clist[i][1]),int(clist[i][2])))