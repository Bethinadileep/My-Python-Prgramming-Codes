#Binary Search Node
class node:
	def __init__(self,x):	
		self.x = x
		self.left = None
		self.right = None


def insert(r, x):
	if r == None:
		return node(x)
	if x <= r.key:
		r.left = insert(r.left, x)
	else:
		r.right = insert(r.right,x)
	return r	
	
root = None

while (True):
	print("1. Insert")
	ch = int(input())
	if ch == 1:
		root = insert(root,int(input("Key:")))
	else:
		break
