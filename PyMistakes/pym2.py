class A():
    x=1
class B(A):
    pass
class C(B):
    pass
B.x=2
A.x=3
print(A.x,B.x,C.x)
