class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort => return(s.sort()=t.sort())
        # return ("".join(sorted(s)) == "".join(sorted(t)))

        frequency = {}
        for char in s:
            if not frequency.get(char):
                frequency[char] = 0
            frequency[char]+=1
        
        for char in t:
            if not frequency.get(char) or frequency[char] == 0:
                return False
            else:
                frequency[char] -= 1
        for key in frequency:
            if frequency[key] != 0:
                return False
        return True
