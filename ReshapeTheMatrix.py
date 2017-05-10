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

def matrixReshape1(nums, r, c):
    flat = sum(nums, [])
    if len(flat) != r * c:
        return nums
    tuples = zip(*([iter(flat)] * c))
    return list(map(list, tuples))

if __name__ == '__main__':
    TEST = [[1, 2], [3, 4], [5, 6], [7 , 8]]
    R = 2
    C = 4
    # R = 4
    # C = 1
    print(matrixReshape(TEST, R, C))
