# 476. Number Complement

> Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

> Note:
> The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.

```
Example 1:

Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

Example 2:

Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
```

## 大意

给定一个数字，将这个数字的二进制表示的每一位翻转，即 0 -> 1, 1 -> 0，最后输出翻转后的数字

## 解决

### Solution 1

```py
def solution1(self, num):
   factor = int('1' * len(bin(num)[2:]), 2)
   return num^factor
```

通过求得 num 的二进制表示的字符串长度，根据长度补 1，最后使用异或求得结果

运行结果： 52ms

### Solution 2

```py
def solution2(self, num):
   return num ^ ((1 << num.bit_length()) - 1)
```

1. 通过 `bit_length()` 方法，求得数字二进制表示字符串的长度（只包含必须的位数，即不包含不必要的 0）。假定求得结果为 L
2. 对 1 向左移位，移位的距离即为 L，记得，这里的移位，会进行补 0 的操作。假定求得结果的十进制表示为 factor
3. 将 factor 减一，假定求得结果为 killer，而 killer 即为 Solution 1 中 “补1” 操作的结果（忽略 factor 减一操作后最左边的 0）
4. 最后还是使用 异或来求的结果

还有很多其他的解决方法，但几乎都是基于对 1 向左移位这一关键步骤实现，移位操作，总比 Solution 1 中的字符串 补1 性能要高吧

