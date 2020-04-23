# 演算法分析機測
# 學號: 10624370/10627130/10627131
# 姓名: 鄭淵哲/林冠良/李峻瑋
# 中原大學資訊工程系
# Sudoku Problem
# Find the solution of sudoku

import numpy as np

class Sudoku():
    def __init__(self, board): # initiate the sudoku board
        self.board = board

        self.size = len(self.board[0])
        # set missing box as 1, known box as -1
        self.choices = [-1 if self.board[i][j] else 1
                        for i in range(self.size)
                        for j in range(self.size)]
        
        self.x = 0
        self.y = 0

    def plot(self): # print out the solution
        for row in self.board:
            for digits in row:
                print(digits, end = '')
            print("")

    def row(self, n): # return the row(y) of the current posotion
        return n in self.board[self.y]

    def col(self, n): # return the column(x) of the current posotion
        return n in [self.board[_][self.x]
                     for _ in range(9)]

    def square(self, n): # return the cordinates in the current square
        return n in [self.board[b][a]
                     for a in range(self.x//3*3, self.x//3*3+3)
                     for b in range(self.y//3*3, self.y//3*3+3)]

    def collision(self, n): # check if there's any same elements in the row, column or square
        if self.row(n) or\
           self.col(n) or\
           self.square(n):
            return True
        else: return False

    def backward(self): # walk backward the matrix
        self.board[self.y][self.x] = 0
        self.choices[self.c] = 1
        if self.x == 0:
            self.x = 8
            self.y -= 1
        else:
            self.x -= 1

        while self.choices[self.y * self.size + self.x] == -1:
            if self.x == 0:
                self.x = 8
                self.y -= 1
            else:
                self.x -= 1

    def forward(self): # walk forward the matrix
        if self.x == 8:
            self.x = 0
            self.y += 1
        else:
            self.x += 1

    def isEnd(self): # check if the sudoku is solved or not
        for row in self.board:
            if 0 in row:
                return False

        return True

    def run(self):
        while not self.isEnd():
            self.c = self.y*self.size+self.x
            if self.choices[self.c] != -1: # if the sudoku needs to be solved
                if self.collision(self.choices[self.c]): # check if there's any same elements
                    # Error
                    if self.choices[self.c] != 9: # check if everybox is solved(1*9=9)
                        self.choices[self.c] += 1
                        continue
                    # Back
                    else: # if not, backward
                        self.backward()

                # Success
                else: # if no collision, fill in
                    self.board[self.y][self.x] = self.choices[self.c]
                    # plot()

                    self.forward()

            else: # no need to be solved, next matrix
                self.forward()

        self.plot()


if __name__ == '__main__':
    w = 9
    h = 9
    board = [[0 for x in range(w)] for y in range(h)] # set the 9x9 board
    for i in range(9): # fill in the values
        singleColumn = []
        singleLine = input()
        for digits in singleLine:
            singleColumn.append(int(digits))
        board[i] = singleColumn

    print("\n")
    s = Sudoku(board)
    s.run()

'''
530070000
600195000
098000060
800060003
400803001
700020006
060000280
000419005
000080079
'''