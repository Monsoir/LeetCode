# 412. Fizz Buzz

> Write a program that outputs the string representation of numbers from 1 to n.

> But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

```
Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
```

## 大意

给出一个数n，输出 1 到 n 的数字字符串表示，其中，某个数为 3 倍数，则使用 "Fizz" 代替，某个数是 5 的倍数，则使用 "Buzz" 代替，某个数既是 3 的倍数，又是 5 的倍数，则作用 "FizzBuzz" 代替

## 解决

### Solution 1

```py
def solution1(n):
    results = []
    for i in range(1, n+1):
        flag = 0
        if i % 3 == 0:
            flag += 3
        if i % 5 == 0:
            flag += 5
        
        results.append(representation(i, flag))
    
    return results

def representation(n, flag):
    switcher = {
        3: 'Fizz',
        5: 'Buzz',
        8: 'FizzBuzz',
    }

    return switcher.get(flag, str(n))
```

很规矩，就是对每一个数进行判断

### Solution 2

```py
def solution2(n):
    return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]
```

惊呆了，更 Pythonic

利用 `aString` * n 这个重复字符串的方法循环产生字符串

`not i % 3` 当 i 为 3 的倍数时，结果为 `False`，则表示 "Fizz" 重复 0 次，也就没有

同时，`... or str(i)`，如果有 "Fizz" 或 "Buzz" 的话，or 语句由于短路而不会执行 `str(i)`，也就没有了数字输出

