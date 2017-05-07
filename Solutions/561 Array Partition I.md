# 561. Array Partition I

> Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

```
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4.
```

> Note:
> n is a positive integer, which is in the range of [1, 10000].
> All the integers in the array will be in the range of [-10000, 10000].

## 大意

给定一个包含 2n 个数字的数组，将数字们分成 n 组，从每组数字中，选取最小的一个数，求得它们相加结果最大值

## 关键思路

将数组进行排序，按顺序分组

### 为什么

![](http://ww1.sinaimg.cn/large/006tNbRwly1ffair0gu4hj31gy0cudk7.jpg)

## Solution 1

```py
def solution1(self, nums):
   inner_num = sorted(nums)
   sum = 0
   for i in range(0, len(nums), 2):
       sum += inner_num[i]
```

## Solution 2

```py
def solution2(self, nums):
   nums.sort()
   return sum(nums[i] for i in range(0, len(nums)) if i % 2 == 0)
```

这种写法更加 Pythonic，但是运行时间更长 (158 ms > 128 ms)

## Reference

[http://blog.csdn.net/whl_program/article/details/70667333](http://blog.csdn.net/whl_program/article/details/70667333)

