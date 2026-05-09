class Solution:
    def trap(self, height: List[int]) -> int:
        prevH, curH, ans = 0, 0, 0
        l, r = 0, len(height)-1
        while(l <= r):
            curH = min(height[l], height[r])
            # print(f"l: {l}, r: {r}, curH: {curH}, prevH: {prevH}")
            if curH > prevH:
                ans+=(curH-prevH)*(r-l+1)
                # -min(height[l], height[r], curH))
                # print(f"+={(curH-prevH)*(r-l+1)}")
            
            if height[l] <= height[r]:
                ans-=min(height[l], max(curH, prevH))
                # print(f"-={min(height[l], max(curH, prevH))}")
                l+=1
            else:
                ans-=min(height[r], max(curH, prevH))
                # print(f"-={min(height[r], max(curH, prevH))}")
                r-=1
            if curH>prevH:
                prevH = curH
        return ans
            
