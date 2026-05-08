class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cur, longest = 0, 0
        nums.sort()
        print(nums)
        for i in range(0, len(nums), 1):
            print(f"i: {i}, cur: {cur}, longest: {longest}")
            if cur == 0:
                cur = 1
            elif nums[i] == nums[i-1]+1:
                cur+=1
            elif nums[i] == nums[i-1]:
                continue
            else:
                cur = 1
            if cur > longest:
                longest = cur
            
        return longest
        