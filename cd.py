t=int(input())

def odd_divisior(x,y):
    k=0
    z=0
    for i in range(x,y+1):
        for j in range(1,y+1):
            if i%j==0:
                k+=1
        if k%2==1:
            z=z+1
        k=0
    print(z)
for i in range(t):
    x,y=input().strip().split()
    odd_divisior(int(x),int(y))
