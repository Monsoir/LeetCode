# 500. Keyboard Row

> Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

![](https://leetcode.com/static/images/problemset/keyboard.png)

```
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
```

> Note:
> You may use one character in the keyboard more than once.
> You may assume the input string will only contain letters of alphabet.

## 大意

给定一个数组，其中包含了若干个单词，找出满足可以在美式键盘上英语字母中一行可以拼写出来的单词

## 解决

```py
FIRSTROW = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
SECONDROW = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
THIRDROW = ['z', 'x', 'c', 'v', 'b', 'n', 'm']

def findWords(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    results = []
    for word in words:
        if allInRow(FIRSTROW, word) or allInRow(SECONDROW, word) or allInRow(THIRDROW, word):
            results.append(word)

    return results

def allInRow(row, word):
    for letter in word.lower():
        if letter in row:
            continue
        else:
            return False

    return True

```

暴力循环


