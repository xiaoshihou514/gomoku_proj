import time

loop = [5,4,3,2]
while True:
    t1=loop[0]-loop[1]
    t2=loop[1]-loop[2]
    t3=loop[2]-loop[3]
    t4=loop[3]-loop[0]
    loop[0]=t1
    loop[1]=t2
    loop[2]=t3
    loop[3]=t4
    print(loop)
    time.sleep(1)