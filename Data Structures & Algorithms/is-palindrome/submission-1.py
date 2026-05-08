class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while(i < j):
            while i < len(s) and not s[i].isalnum():
                i+=1
            while j >= 0 and not s[j].isalnum():
                j-=1
            # print(f"i: {i}, j: {j}, s[i]: {s[i]}, s[j]: {s[j]}")
            if(i<len(s) and j >= 0):
                if s[i].lower() == s[j].lower():
                    i+=1
                    j-=1
                else:
                    return False
        return True
        