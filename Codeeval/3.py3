# palindrome
import math
def palindrome_dgt(d):
    if str(d)==str(d)[::-1]:
        return True
    
def prime():
    prime=[]
    for  i in range(2,1000):
        r=int(math.sqrt(i))+1
        for j in range(2,r+1):
            if i%j==0:
                break
            elif i%j!=0 and j==r:
                prime.append(i)
    z=0
    for i in prime:
        if palindrome_dgt(i):
            z=i
    print(z)
prime()
