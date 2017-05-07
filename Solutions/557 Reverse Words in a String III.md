# 557. Reverse Words in a String III

> Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

```
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
```

> Note: In the string, each word is separated by single space and there will not be any extra space in the string.

## 大意

输入一个字符串，这个字符串使用空格区分每个单词，将字符串中的每个单词字母排列顺序反转

## 解决

### Solution 1

```py
def solution1(self, s):
   raw_materials = s.split(' ')
   materials = []
   for foo in raw_materials:
       fo = foo[::-1]
       materials.append(fo)
   
   return ' '.join(materials)
```

### Solution 2

```py
def solution2(self, s):
   return " ".join([foo[::-1] for foo in s.split(' ')])
```

此方法更加 Pythonic

