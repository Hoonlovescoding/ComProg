mname = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
zod = ["Aries","Taurus","Gemini","Cancer","Leo","Virgo","Libra","Scorpio","Sagittarius","Capricorn","Aquarius","Pisces"]
daym = [31,0,31,30,31,30,31,31,30,31,30,31]

def read_date():
    date1 = input().split()
    d1, m1, y1=int(date1[0]), mname.index(date1[1][:3])+1, int(date1[2])
    return [d1,m1,y1]

def zodiac(d,m):
    if (d >= 22 and 3 <= m <= 12) or (d >= 21 and 1 <= m <= 2):
        z = zod[m-3]
    elif (d <= 21 and 4 <= m <= 12) or (d <= 20 and 1 <= m <= 2) or (d <= 21 and m==3):
        z= zod[m-4]
    return z

def days_in_feb(y):
    if y % 400 == 0 or y % 100 != 0 and y % 4 == 0:
        d = 29
    else:
        d = 28
    return d

def days_in_month(m,y):
    daym[1] = days_in_feb(y)
    d = daym[m-1]
    return d

def days_in_between(d1,m1,y1,d2,m2,y2):
    a1=d1
    a2=d2
    dy=0
    while y1 < y2:
        for i in range(12):
            dy+= days_in_month(i+1,y1)
        y1+=1
    for i in range(m1-1):
        a1+=days_in_month(i+1,y1)
    for i in range(m2-1):
        a2+=days_in_month(i+1,y2)
    return a2-a1+dy-1

def main():
    d1,m1,y1 = read_date()
    d2,m2,y2 = read_date()
    print(zodiac(d1,m1)+' '+zodiac(d2,m2))
    print(days_in_between(d1,m1,y1,d2,m2,y2))
    
exec(input().strip())
