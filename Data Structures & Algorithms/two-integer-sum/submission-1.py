class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {nums[0]: 0}
        
        for i in range(1, len(nums)):
            # print(index)
            # print("index.get(target-nums[i]): ", index.get(target-nums[i]))
            if index.get(target-nums[i]) is not None:
                return [index[target-nums[i]], i]
            else:
                index[nums[i]] = i