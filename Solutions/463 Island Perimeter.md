# [463. Island Perimeter](https://leetcode.com/problems/island-perimeter/#/description)

> You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.


```
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:
```

![](https://leetcode.com/static/images/problemset/island.png)


## 大意

给定一个二维数组，里面的值都是 1 或 0，这个二维数组可以映射成一个大的矩形，而这个大的矩形由长度为 1 的正方形组成，其中值为 1 的可以映射成矩形里面的陆地，而陆地的组合形成一个岛，而其他值为 0 的，映射成水

这些陆地的排列只有横和竖，没有斜的，求给定的一个二维数组中，陆地的边长 

## 解决

### Solution 1

```py
def solution1(grid):
    rounds = len(grid)
    rowRounds = len(grid[0])
    length = 0
    for i in range(0, rounds):
        for j in range(0, rowRounds):
            if grid[i][j] == 1:
                if i == 0:
                    length += 1
                if j == 0:
                    length += 1
                if i == rounds-1:
                    length += 1
                if j == rowRounds - 1:
                    length += 1

                if i > 0 and grid[i-1][j] == 0:
                    length += 1
                if i < rounds - 1 and grid[i+1][j] == 0:
                    length += 1
                if j > 0 and grid[i][j-1] == 0:
                    length += 1
                if j < rowRounds - 1 and grid[i][j+1] == 0:
                    length += 1

    return length
```

暴力解决

针对值为 1 的正方形：

1. 先检查是否位于边上，若是，则 length 加上 1（因为肯定有边缘这一长度）
2. 依次检查这当前正方形的四周，若为 0，则 length 加上 1（因为对应的边已经暴露了，成为了边缘）



### Solution 2

```py
import operator
def islandPerimeter(self, grid):
    return sum(sum(map(operator.ne, [0] + row, row + [0]))
               for row in grid + map(list, zip(*grid)))
```

这个 Solution 目测只适合运行在 Python 2.7，然而，这个解法非常有意思

[原答案链接](https://discuss.leetcode.com/topic/68778/short-python)

---

总体思路

根据题目原文意思，陆地中是没有湖的，这意味着不同数值的组合（即 01 或 10），它们共同拥有的边便是边缘，也意味着，计算边缘的长度，等于计算 01 或 10 组合的个数，无论是水平方向还是垂直方向

---

生成所有的 list

由于要计算水平方向与垂直方向的不同组合个数，水平方向的数据是比较容易获取的，传入的参数 grid 本身就可以看作是一个水平方向的数据

而垂直方向的数据，可以通过 Python 的 `zip` 函数来将 grid (grid 是二维数组)的相同 index 的值组成一个元素，从而又组成一个 list

由于 zip 返回的是一个 iterator，因此需要将 iterator 转换为 list，通过 `map` 对每个号元素执行 `list` 方法

于是有了

```py
# 这里注意，遍历的是 list 与 map(list, zip(*grid)) 组成的 list
for row in grid + map(list, zip(*grid))
# 也可以看作是
# for row in (grid + map(list, zip(*grid)))
```

在 Python 3.x 中，`map` 返回的是一个 iterator，因此，转换成 list

```py
for row in grid + list(map(list, zip(*grid)))
```

于是，对于 grid 的输入为

```py
[0, 1, 0, 0]
[1, 1, 1, 0]
[0, 1, 0, 0]
[1, 1, 0, 0]
```

可得出最后的结果为：

```py
[0, 1, 0, 0]
[1, 1, 1, 0]
[0, 1, 0, 0]
[1, 1, 0, 0]
[0, 1, 0, 1]
[1, 1, 1, 1]
[0, 1, 0, 0]
[0, 0, 0, 0]
```

---

map(operator.ne, [0] + row, row + [0])

通过 `map` 对 [0] + row 与 row + [0] 中的每一个元素执行一个 operation.ne 的运算，其中 `operation.ne` 可以看作是一个 不相等就为 True 的一个运算(Not Equal)

> 可参考 [官方文档说明](https://docs.python.org/3/library/operator.html#operator.__ne__)

而 [0] + row 与 row + [0] 则分别为 row 的前面和后面补上一个 0，并形成两个新的相应的 list

即，对于 [0, 1, 0, 0]，得出的结果为 

```py
map(operator.ne, [0, 0, 1, 0, 0], [0, 1, 0, 0 ,0])
```

这里的比较，个人感觉也就是这个解法中最有趣的部分了

想象到运算的过程：

```
0 0 1 0 0
0 1 0 0 0
----ne----
F T T F F
```

这里，运用了一个 trick，就可以很直观地让 [0, 1, 0, 0] 中的每一个元素，与这个元素的前后元素进行 `operation.ne` 的运算，同时，还方便地前后补 0，考虑到边界的情况，这看起来很像 移位

---

最后，`map` 出来的结果富含 `True` 和 `False`，这些值，又回映射成 1 和 0 来送入到 `sum` 进行运算

这样，就可以顺利地将水平方向的每一个数据和垂直方向的每一个数据进行核算，最后，最外层的 `sum` 就将这两个方向的每一组数据相加，得出结果

---


