class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixMult, postFixMult = 1,1
        res = [1]*len(nums)
        # mult before/after i
        for i in range(1, len(nums)):
            prefixMult*=nums[i-1]
            res[i]*=prefixMult
        for i in range(len(nums)-2, -1, -1):
            postFixMult*=nums[i+1]
            res[i]*=postFixMult
        # for i in range(0, len(nums)):
        #     prefixMult[i] = prefixMult[i]*postFixMult[i]
        return res