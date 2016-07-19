class PairSum:
    def __init__(self,arr,k):
        self.arr=arr
        self.k=k
        self.process(self.arr,self.k)
    def process(self,ar,k):
        self.z=0
        for i in range(len(ar)):
            for j in range(i+1,len(ar)):
                if ar[i]+ar[j]==k:
                    self.z=self.z+1
                    print(ar[i],ar[j],self.z)
        print(self.z)

p=PairSum
p([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10)
