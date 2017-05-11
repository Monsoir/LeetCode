# 496. Next Greater Element I

> You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

```
Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
```

```
Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
```

> Note:
> All elements in nums1 and nums2 are unique.
The length of both nums1 and nums2 would not exceed 1000.

## 大意

给定两个数组，num1, num2，其中，num1 中的数据 num2 中的数据的子集，并且 num1 和 num2 中都没有重复的数据

对于 num1 中的每一个数据 x，在 num2 中定位 x 的位置，并且找出 x 右边第一个比 x 大的数，如果没有比 x 大的数，那对应的值为 -1，最后输出这些值

## 解决

### Solution 1

```py
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
```

暴力求解

对 findNums 中的每一个元素，在 nums 中定位后，不断比较该元素在 nums 中右边元素

149ms

### Solution 2

```py
from collections import deque
def solution2(findNums, nums):
    aStack = deque()
    aDict = dict()
    for i in range(len(nums)-1, -1, -1):
        while aStack:
            val = aStack[-1]
            if nums[i] < val:
                aDict[nums[i]] = val
                break
            else:
                aStack.pop()

        if not aStack:
            aDict[nums[i]] = -1
        aStack.append(nums[i])
    return [aDict[x] for x in findNums]
```

理解这种解法的关键

- 首先在 nums 中处理好 findNums 中的每一个元素的结果，放到 Dict 中，而不是一开始就用 findNums 中的数据处理
- 其实，会将 nums 中所有元素的右边第一个最大值求出来，并且放在了 dict 中，最后通过 findNums 中，通过 key-value 读取相应的元素
- aStack 是一个栈，并且其中的元素值是递减（索引由小到大）的，用来找出每次遍历时，当前元素的最大值
- 需确保，当前遍历的元素 x，与当前栈顶元素 A 的关系为 x < A，否则，将 A 从栈中弹出


这个方法快很多了，49ms


![](http://ww1.sinaimg.cn/large/006tNbRwgy1ffhqpkh2u8j30n50wytbi.jpg)

