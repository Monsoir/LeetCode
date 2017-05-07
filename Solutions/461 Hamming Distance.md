# 461. Hamming Distance

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

## 大意

给定两个数字，找出他们二进制表示对应位置不相等的位个数

## 解决

### Solution 1

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

### Solution 2

```py
def solution2(self, first, second):
   third = first^second
   return bin(third).count('1')
```

直接使用异或，然后将结果转成二进制字符串，统计 1 的个数，异或是位相等时位0，不相等时为 1

