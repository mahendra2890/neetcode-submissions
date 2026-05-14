class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        countS1 = defaultdict(lambda: 0)
        countS2 = defaultdict(lambda: 0)
        uniqueCharsS1 = set()
        uniqueCharsS2 = set()
        for c in s1:
            countS1[c]+=1
            uniqueCharsS1.add(c)
        start, end = 0, 0
        while end < len(s2):
            # print(uniqueCharsS2)
            # print(s2[end])
            if (end-start+1) < len(s1):
                # print("Not complete yet")
                # something
                uniqueCharsS2.add(s2[end])
                countS2[s2[end]]+=1
                end+=1
            else:
                # print("complete")
                # we have correct size substring, we check whatever we need to check now
                if (countS2[s2[end]] == 0):
                    uniqueCharsS2.add(s2[end])
                countS2[s2[end]]+=1
                
                if uniqueCharsS2 == uniqueCharsS1:
                    same = True
                    for item in countS1:
                        if (countS1[item] != countS2[item]):
                            same = False
                            break
                    if same:
                        return True
                countS2[s2[start]]-=1
                if countS2[s2[start]] == 0:
                    uniqueCharsS2.remove(s2[start])
                end+=1
                start+=1
        return False
