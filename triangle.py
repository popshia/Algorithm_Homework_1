# 演算法分析機測
# 學號: 10624370/10627130/10627131
# 姓名: 鄭淵哲/林冠良/李峻瑋
# 中原大學資訊工程系
# Find Triangle Problem
# Find the number of triangle by input N

import numpy as np
import random

def FindTriangle(num):
    count = 0
    for a in range(1, num + 1):
        for b in range(a, num + 1 ):
            for c in range(b, num + 1 ):
                if a != b and a != c and b !=c and a + b > c : # the three side length conforms the rule
                    count = count + 1
    return count

if __name__ == '__main__':
    num = int(input("Please enter N...\n"))
    answer = []
    while num != 0 :
        if num < 3 or num > 100 :
            print ( "Input error!")
        else :
            answer.append(FindTriangle(num))
        num = int(input())
    print("\n")
    for answer in answer:
        print(answer)
