# 566. Reshape the Matrix

> In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

> You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

> The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

> If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

```
Example 1:
Input: 
nums = 
[[1,2],
 [3,4]]
r = 1, c = 4
Output: 
[[1,2,3,4]]
Explanation:
The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.
```

```
Example 2:
Input: 
nums = 
[[1,2],
 [3,4]]
r = 2, c = 4
Output: 
[[1,2],
 [3,4]]
Explanation:
There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.
```

> Note:
> The height and width of the given matrix is in range [1, 100].
The given r and c are all positive.

## 大意

给定一个二维数组，一个 r 值（实际上是 row），一个 c 值（实际上是 column）。

将这个二维数组按照 r 与 c 重新布局，布局的格式参考例子

## 解决

### Solution 1

```py
def matrixReshape(nums, r, c):
    """
    :type nums: List[List[int]]
    :type r: int
    :type c: int
    :rtype: List[List[int]]
    """
    if canReverse(nums, r, c):
        return rowReversing(nums, r, c)
    return nums

def canReverse(nums, r, c):
    return r * c == len(nums) * len(nums[0])

def rowReversing(nums, r, c):
    temp = []
    result = []
    for row in nums:
        for element in row:
            temp.append(element)

    for index in range(r):
        row = temp[index * c : index * c + c]
        result.append(row)

    return result
```

首先，调用 `canReverse` 来判断原数组是否可以根据 r, c 进行重新布局，如果不能，则直接返回原数组

若原数组可以根据 r, c 进行重新布局，那就重新布局吧，调用 `rowReversing`

在 `rowReversing` 中，
① 现将原数组转化为一维数组，方便后续的读取
② 根据 r, c 将一维数组进行分组

分组的时候，可以看作是一个分页的步骤：

- 将 r 看成是 pages
- 将 c 看成是 pageSize

### Solution 2

```py
import numpy as np

class Solution(object):
    def matrixReshape(self, nums, r, c):
        try:
            return np.reshape(nums, (r, c)).tolist()
        except:
            return nums
```

使用了 Python 的科学计算的库 NumPy，里面直接就提供了 reshape 方法

[NumPy 的链接](http://www.numpy.org)
[numpy.reshape 的链接](https://docs.scipy.org/doc/numpy/reference/generated/numpy.reshape.html)

### Solution 3

```py
def matrixReshape(self, nums, r, c):
    flat = sum(nums, [])
    if len(flat) != r * c:
        return nums
    tuples = zip(*([iter(flat)] * c))
    return map(list, tuples)
```

这个 Solution 与 Solution 1 的思路基本相同，但是实现的方式有出入，充分利用了 Python 标准库中的方法

