# 演算法分析機測
# 學號: 10624370/10627130/10627131
# 姓名: 鄭淵哲/林冠良/李峻瑋
# 中原大學資訊工程系
# Preorder to Postorder Problem
# Build a binary tree from preorder transversal and output as postorder transversal

class Node(): 
	def __init__(self, data): # initial node
		self.data = data 
		self.left = None
		self.right = None
		self.isChar = False

def Construction(preorder, low, high, size):
	if( Construction.index >= size or low > high): # end case
		return None
	root = Node(preorder[Construction.index]) # set root node 
	Construction.index += 1 # increase the visit index
	if low == high: # root case
		return root 
	for i in range(low, high+1): # set visit range
		if preorder[i] > root.data: 
			break
	root.left = Construction(preorder, Construction.index, i-1 , size) # recursive the left node
	root.right = Construction(preorder, i, high, size) # recursive the right node
	return root 

def ConstructTree(preorder): # constuct the tree
	size = len(preorder)
	Construction.index = 0
	return Construction(preorder, 0, size-1, size) 

def PrintPostorder(root, isChar): # print out the postorder transversal of the given root
	if root is None:
		return
	if isChar == False:
		PrintPostorder(root.left, False)
		PrintPostorder(root.right, False)
		print(root.data, end=' ')
	if isChar == True:
		PrintPostorder(root.left, True)
		PrintPostorder(root.right, True)
		print(chr(root.data), end=' ')
		
if __name__ == '__main__':
	answers = []
	nodeValue = list(input().split())
	while len(nodeValue) != 1:
		isChar = False
		preorder = []
		for values in nodeValue:
			if values.isnumeric(): # numeric input
				preorder.append(int(values))
			else: # character input
				isChar = True
				preorder.append(ord(values))
		root = ConstructTree(preorder)
		root.isChar = isChar
		answers.append(root)
		nodeValue = list(input().split())
	for roots in answers: # print out the root(s) in the answer array
		PrintPostorder(roots, roots.isChar)
		print("\r")