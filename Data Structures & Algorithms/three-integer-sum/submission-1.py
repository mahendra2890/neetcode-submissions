class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(0, len(nums)-2, 1):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j, k = i+1, len(nums)-1
            while j < k:
                if nums[j]+nums[k] > -nums[i]:
                    k-=1
                elif nums[j]+nums[k] < -nums[i]:
                    j+=1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    while True:
                        j+=1
                        if j >= len(nums)-1 or nums[j] != nums[j-1]:
                            break
                    while True:
                        k-=1
                        if k < 0 or nums[k] != nums[k+1]:
                            break
                    # k-=1
            
        return res