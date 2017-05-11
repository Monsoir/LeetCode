def nextGreaterElement(findNums, nums):
    """
    :type findNums: List[int]
    :type nums: List[int]
    :rtype: List[int]
    """
    return solution2(findNums, nums)


def solution1(findNums, nums):
    result = []
    for element in findNums:
        index = nums.index(element)
        result.append(findGreaterFor(element, nums, index))

    return result

def findGreaterFor(flag, nums, start):
    for i in range(start, len(nums)):
        if nums[i] > flag:
            return nums[i]

    return -1

from collections import deque
def solution2(findNums, nums):
    aStack = deque()
    aDict = dict()
    for i in range(len(nums)-1, -1, -1):
        while aStack:
            if nums[i] < aStack[-1]:
                aDict[nums[i]] = aStack[-1]
                break
            else:
                aStack.pop()

        if not aStack:
            aDict[nums[i]] = -1
        aStack.append(nums[i])
    
    return [aDict[x] for x in findNums]

# from collections import deque
# def solution2(findNums, nums):
#     aStack = deque()
#     aDict = dict()
#     for i in range(len(nums)-1, -1, -1):
#         while aStack:
#             val = aStack[-1]
#             if nums[i] < val:
#                 aDict[nums[i]] = val
#                 break
#             else:
#                 aStack.pop()

#         if not aStack:
#             aDict[nums[i]] = -1
#         aStack.append(nums[i])
#     return [aDict[x] for x in findNums]


if __name__ == '__main__':
    # num1 = [4,1,2]
    # num2 = [1,3,4,2]
    num1 = [2, 4]
    num2 = [1, 2, 3, 4]

    print(nextGreaterElement(num1, num2))
