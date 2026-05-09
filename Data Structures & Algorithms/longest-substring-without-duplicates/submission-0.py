class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        start, end = 0, 0
        ans = 0
        freq = defaultdict(lambda: 0)
        while(end < len(s)):
            if freq[s[end]] == 0:
                freq[s[end]]+=1
                ans = max(ans, end-start+1)
                end+=1
            else:
                freq[s[start]]-=1
                start+=1
            
        return ans



        