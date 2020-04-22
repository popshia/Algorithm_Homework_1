# 演算法分析機測
# 學號: 10624370/10627130/10627131
# 姓名: 鄭淵哲/林冠良/李峻瑋
# 中原大學資訊工程系
# Grid Puzzle
# using BFS
import collections

class Solution():
	def SlidingPuzzle(self, board):
		start = self.BoardToString(board) # convert board array to a string
		
		BFS = collections.deque() # declare a queue for BFS
		BFS.append((start, 0)) # start is string 
		visited = set() # declare a set to keep track of all the visited situation
		visited.add(start) # string
		stepList = [] # store the total move value of every case
	
		dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] # set the direction values
		
		while BFS:
			path, step = BFS.popleft()
			# pop the elements in queue, path is the panel, step is what the word mean

			if path[0] == "1":
				stepList.append(step) # solved case, add the steps to stepList

			p = path.index("0") # find 0
			x, y = int(p / 3), p % 3 # x, y cordinates
			path = list(path) # set path as list
			for dir in dirs: # switch elements of current situation
				tx, ty = x + dir[0], y + dir[1]
				if tx < 0 or tx >= 3 or ty < 0 or ty >= 3: # if the moving range is greater than the panel, skip
					continue
				path[int(x * 3 + y)], path[int(tx * 3 + ty)] = path[int(tx * 3 + ty)], path[int(x * 3 + y)] # swap elements
				pathString = "".join(path)
				if pathString not in visited: # if the steps isn't found yet, add to the BFS queue
					BFS.append((pathString, step + int(path[int(x * 3 + y)])))
					visited.add(pathString) # push into visited
				path[int(x * 3 + y)], path[int(tx * 3 + ty)] = path[int(tx * 3 + ty)], path[int(x * 3 + y)] # swap the elements back
		return stepList # return stepList
	
	def BoardToString(self, board):
		boardString = ""
		for i in range(3):
			for j in range(3):
				boardString += str(board[i][j])
		return boardString

def main():
	obj1 = Solution()

	digits = []
	print("Please input your slide puzzle panel...")
	for _ in range(3):
		#digit = input().split()
		digit = [int(i) for i in input().split()]
		digits.append(digit)

	digit_panel = [digits[0],digits[1],digits[2]]
	
	stepList = obj1.SlidingPuzzle(digit_panel)
	answer = 10000
	for step in stepList : # find the minimum move cost
		if step < answer : 
			answer = step
			
	print("Minimum Sum of Costs =", answer)

if __name__ == "__main__" :
	main()