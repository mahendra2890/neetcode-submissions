class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums) == 0):
            return 0
        longestEndingAt = [1]*len(nums)
        longest = 1
        nums.sort()
        for i in range(0, len(nums), 1):
            for j in range(0, i, 1):
                if nums[i] == nums[j]+1:
                    longestEndingAt[i] = max(longestEndingAt[i], longestEndingAt[j]+1)

            longest = max(longest,longestEndingAt[i])
        return longest