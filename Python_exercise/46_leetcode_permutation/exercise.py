class Solution(object):
    def permute(self, nums):
        if len(nums) <= 1:
            return [nums]

        result = []
        for i, num in enumerate(nums):
            n = nums[:i] + nums[i+1:]
            for j in self.permute(n):
                result.append([num] + j)
        return result

s = Solution()
print(s.permute([3, 4, 5, 6]))
