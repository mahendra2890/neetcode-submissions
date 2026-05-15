class Solution:
    def isWindowValid(self, countWindow: dict, k: int) -> bool:
        maxFreq = 0
        totalCount = 0
        for item in countWindow:
            totalCount+=countWindow[item]
            if countWindow[item] > maxFreq:
                maxFreq = countWindow[item]
        totalCount-=maxFreq
        return totalCount <= k
        
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, -1
        countWindow = defaultdict(lambda: 0)
        ans = 0
        while r <= len(s):
            # print(f"l: {l}, r: {r}, countWindow: {dict(countWindow)}")
            # [l, r] is the window
            if self.isWindowValid(countWindow, k):
                if r != -1 and l <= r:
                    # current window is valid: lenWindow = r-l+1
                    ans = max(ans, r-l+1)
                if r == len(s)-1:
                    break
                r+=1
                countWindow[s[r]]+=1
            else:
                countWindow[s[l]]-=1
                l+=1
        return ans