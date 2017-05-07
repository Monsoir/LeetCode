class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """

        return self.solution2(num)

    def solution1(self, num):
        factor = int('1' * len(bin(num)[2:]), 2)
        return num^factor

    def solution2(self, num):
        return num ^ ((1 << num.bit_length()) - 1)

if __name__ == '__main__':
    TEST = 5
    S = Solution()
    print(S.findComplement(TEST))