class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort => return(s.sort()=t.sort())
        return (sorted(s) == sorted(t))