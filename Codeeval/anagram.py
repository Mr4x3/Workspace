class anagram:
    def __init__(self,s1,s2):
        self.s1=s1.replace(' ','')
        self.s2=s2.replace(' ','')
        k=self.check(self.s1,self.s2)
        print(k)
    def check(self,ps1,ps2):
        for i in ps1:
            if i not in ps2:
                return False
        return True

a=anagram
a('dogil','godl')
