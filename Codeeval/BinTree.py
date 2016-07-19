class B:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def setData(self,data):
        self.data=data

def pre(root,result):
	if not root:
		return
	result.append(root.data)
	pre(root.left,result)
	pre(root.right,result)
	return result
	



k=B(1)
k.left=B(2)
k.right=B(3)
k.left.left=B(4)
k.left.right=B(5)
k.right.left=B(6)
k.right.rigth=B(7)
k.left.left.left=B(8)
print(pre(k,[]))
