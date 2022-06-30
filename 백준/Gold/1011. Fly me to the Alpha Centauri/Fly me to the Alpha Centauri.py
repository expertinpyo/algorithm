import sys
num = int(input())
while num:
    x,y = map(int,sys.stdin.readline().split())
    distance = y-x
    if distance <=2:
        print(distance)
    else:
        n=3
        z=n
        a=3
        s=3
        while True:
            dn=2*n
            if distance <= dn:
                if distance <=(int((dn-z)*0.5))+z:
                    print(s)
                else:
                    print(s+1)
                break
            else:
                z=n*2
                n+=a
                a+=1
                s+=2
    num-=1
