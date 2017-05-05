class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        return self.solution2(nums)

    def solution1(self, nums):
        inner_num = sorted(nums)
        sum = 0
        for i in range(0, len(nums), 2):
            sum += inner_num[i]
        
        return sum
    def solution2(self, nums):
        nums.sort()
        return sum(nums[i] for i in range(0, len(nums)) if i % 2 == 0)


if __name__ == '__main__':
    # nums = [5, 2, 3, 1, 4, 6]
    nums = [1,4,3,2]
    s = Solution()
    print(s.arrayPairSum(nums))