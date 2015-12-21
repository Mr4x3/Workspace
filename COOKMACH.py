t=int(input())

def cm(q,r):
    ans=0
    if q==r:
        ans=0
    else:
        while q!=r:
            if q==1:
                while q!=r:
                    q=q*2
                    ans=ans+1
                    continue
            elif q%2==0 and r>q:
                q=q*2
                ans=ans+1
                continue
            elif q%2==0 and r<q:
                q=q/2
                ans=ans+1
                continue

            else:
                q=(q-1)/2
                ans=ans+1
                continue
    return ans
                
                
for i in range(t):
    q,r=input().strip().split()
    q,r=int(q),int(r)
    print(cm(q,r))
