class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        doesExist = {}
        for num in nums:
            if doesExist.get(num) == True:
                return True
            else:
                doesExist[num] = True
        return False