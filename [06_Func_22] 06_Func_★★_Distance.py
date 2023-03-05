def distance1(x1,y1,x2,y2):
    dis = ((x1-x2)**2+(y1-y2)**2)**0.5
    return dis

def distance2(p1, p2):
    dis = ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5
    return dis

def distance3(c1, c2):
    dis = ((c1[0]-c2[0])**2+(c1[1]-c2[1])**2)**0.5
    if dis <= c1[2]+c2[2]:
        return dis, True
    else:
        return dis, False

def perimeter(points):
    dis = 0
    for i in range(len(points)):
        dis += ((points[i-1][0]-points[i][0])**2+(points[i-1][1]-points[i][1])**2)**0.5
    return dis

exec(input().strip())