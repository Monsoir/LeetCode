class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return self.solution2(x, y)

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

    def solution2(self, first, second):
        third = first^second
        return bin(third).count('1')


if __name__ == '__main__':
    A = 1
    B = 4

    SOLUTION = Solution()
    RESULT = SOLUTION.hammingDistance(A, B)
    print(RESULT)
