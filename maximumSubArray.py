# 演算法分析機測
# 學號: 10624370/10627130/10627131
# 姓名: 鄭淵哲/林冠良/李峻瑋
# 中原大學資訊工程系
# Maximum Subarray Problem
# Find the maximum subarray

from array import array

def FindMaximumSubarray(A):
    n = len(A)
    low, high, sum = Find(A, 0, n - 1)

    print("Maximum Subarray Problem:")
    print("Low =", low+1, "High =", high+1, "Sum =", sum)


def Find(A, low, high):
    if high == low:
        return low, high, A[low]
    else:
        mid = (low + high) // 2
        # devide and conquer
        left_low, left_high, left_sum = Find(A, low, mid) # check left part sum
        right_low, right_high, right_sum = Find(A, mid + 1, high) # check right part sum
        cross_low, cross_high, cross_sum = FindCrossingArray(A, low, mid, high) # check cross(mid) part sum
        # fnd the largest sum
        if (left_sum > right_sum and left_sum >= cross_sum):
            return left_low, left_high, left_sum
        elif (right_sum >= left_sum and right_sum >= cross_sum):
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


def FindCrossingArray(A, low, mid, high):
    left_sum = -3000000
    sum = 0
    for i in range(mid, low - 1, -1): # add left values
        sum += A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i

    right_sum = -3000000
    sum = 0
    for j in range(mid + 1, high + 1): # add right values
        sum += A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j

    # set low, high indexs and the sum of the range
    cross_low = max_left
    cross_high = max_right
    cross_sum = left_sum + right_sum

    return cross_low, cross_high, cross_sum

if __name__ == '__main__':
    wholeArray = array('i', [])
    n = int(input("Please enter N...\n"))
    arrayValue = map(int,input("Please enter array values...\n").split())
    for value in arrayValue:
        wholeArray.append(value)
    FindMaximumSubarray(wholeArray)
