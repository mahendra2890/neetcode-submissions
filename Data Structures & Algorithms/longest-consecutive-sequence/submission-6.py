class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        res = 0
        vis = set()
        for num in nums:
            # print(num)
            # print(mp)
            if num not in vis:
                temp = mp[num - 1] + mp[num + 1] + 1
                # print(num - mp[num - 1])
                # print(num + mp[num + 1])
                mp[num - mp[num - 1]] = temp
                mp[num + mp[num + 1]] = temp
                res = max(res, temp)
                vis.add(num)
            # print(mp)
            
        return res