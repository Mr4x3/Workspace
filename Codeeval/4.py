# By Sieve of Eratosthenes
Till=8000
def prime(Till):
    primes=[True for i in range(Till)]
    primes[0]=primes[1]=False
    for i in range(1, int(Till ** .5 + 1)):
        if primes[i]:
            for j in range(i**2, Till, i):
                primes[j]=False
    return primes

k=prime(Till)
z=0
a=[]
h=1000
for i in range(Till):
    if k[i]:
        a.append(i)
print(sum(a[0:1000]))

