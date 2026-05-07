class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixMult, postFixMult = [1]*len(nums), [1]*len(nums)
        # mult before/after i
        for i in range(1, len(nums)):
            prefixMult[i] = prefixMult[i-1]*nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            postFixMult[i] = postFixMult[i+1]*nums[i+1]
        for i in range(0, len(nums)):
            prefixMult[i] = prefixMult[i]*postFixMult[i]
        return prefixMult