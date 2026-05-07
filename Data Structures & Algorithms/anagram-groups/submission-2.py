class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create dict: sorted(anagram), [values] -> create array of [values per anagram] -> return
        anagramStringSubLists = defaultdict(lambda: [])
        for item in strs:
            key = "".join(sorted(item))
            # nlogn
            anagramStringSubLists[key].append(item)
            # 1: list contains pointers and not exact values of items - when we do extend that is when everything needs to be copied.
        # for key in anagramStringSubLists:
        return list(anagramStringSubLists.values())
        