class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False
        nums.sort()
        for i in range(1, len(nums), 1):
            if nums[i] == nums[i-1]:
                return True
        return False
        