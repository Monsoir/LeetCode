class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        return self.solution2(s)

    def solution1(self, s):
        raw_materials = s.split(' ')
        materials = []
        for foo in raw_materials:
            fo = foo[::-1]
            materials.append(fo)
        
        return ' '.join(materials)
    
    def solution2(self, s):
        return " ".join([foo[::-1] for foo in s.split(' ')])


if __name__ == '__main__':
    TEST = "Let's take LeetCode contest"
    S = Solution()
    print(S.reverseWords(TEST))