class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = defaultdict(lambda: 0)
        uniqueT = 0
        for c in t:
            countT[c]+=1
            if countT[c] == 1:
                uniqueT+=1
        l, r = 0, 0
        countS = defaultdict(lambda: 0)
        countTinS = 0
        ansL, ansR = -1, len(s)
        while r <= len(s):
            # print(f"l: {l}, r: {r}, ansL: {ansL}, ansR = {ansR}, countTinS: {countTinS}, uniqueT: {uniqueT}")
            if countTinS == uniqueT:
                # move l ahead, and keep on updating min
                if (ansR-ansL) >= (r-l):
                    ansR = r
                    ansL = l
                countS[s[l]]-=1
                if countT[s[l]] != 0 and countT[s[l]] == (countS[s[l]]+1):
                    countTinS-=1
                l+=1
                
            else:
                if r == len(s):
                    # print(f"BREAKING: l: {l}, r: {r}, ansL: {ansL}, ansR = {ansR}, countTinS: {countTinS}, uniqueT: {uniqueT}")
            
                    break;
                # add r, update counts, see if valid
                countS[s[r]]+=1
                if countT[s[r]] != 0 and countT[s[r]] == (countS[s[r]]):
                    countTinS+=1
                r+=1
        if ansL != -1:
            return s[ansL:ansR]
        return ""


        