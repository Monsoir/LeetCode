# LeetCode 解题记要

- [461. Hamming Distance](461-hammingdistance)
- [561. Array Partition I](561-arraypartitioni)

## 461. Hamming Distance

> The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

> Given two integers x and y, calculate the Hamming distance.

> Note:
> 0 ≤ x, y < 231.

```
Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
```

### 大意

给定两个数字，找出他们二进制表示对应位置不相等的位个数

### 解决

#### Solution 1

```py
def solution1(self, x, y):
   x_str = bin(x)[-1:1:-1].ljust(31, '0')
   y_str = bin(y)[-1:1:-1].ljust(31, '0')

   print(x_str)
   print(y_str)

   count = 31
   loop = 31

   for i in range(loop):
       if x_str[i] == y_str[i]:
           count -= 1

   return count
```

直接把数字转成二进制字符串，然后需要补0，最后使用字符串的比较

#### Solution 2

```py
def solution2(self, first, second):
   third = first^second
   return bin(third).count('1')
```

直接使用异或，然后将结果转成二进制字符串，统计 1 的个数，异或是位相等时位0，不相等时为 1

## 


## 561. Array Partition I

> Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

```
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4.
```

> Note:
> n is a positive integer, which is in the range of [1, 10000].
> All the integers in the array will be in the range of [-10000, 10000].

### 大意

给定一个包含 2n 个数字的数组，将数字们分成 n 组，从每组数字中，选取最小的一个数，求得它们相加结果最大值

### 关键思路

将数组进行排序，按顺序分组

##### 为什么

![](http://ww1.sinaimg.cn/large/006tNbRwly1ffair0gu4hj31gy0cudk7.jpg)

### Solution 1

```py
def solution1(self, nums):
   inner_num = sorted(nums)
   sum = 0
   for i in range(0, len(nums), 2):
       sum += inner_num[i]
```

### Solution 2

```py
def solution2(self, nums):
   nums.sort()
   return sum(nums[i] for i in range(0, len(nums)) if i % 2 == 0)
```

这种写法更加 Pythonic，但是运行时间更长 (158 ms > 128 ms)

### Reference

[http://blog.csdn.net/whl_program/article/details/70667333](http://blog.csdn.net/whl_program/article/details/70667333)


