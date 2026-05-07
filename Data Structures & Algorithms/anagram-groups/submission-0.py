class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create dict: sorted(anagram), [values] -> create array of [values per anagram] -> return
        anagramStringSubLists = {}
        for item in strs:
            key = "".join(sorted(item))
            if anagramStringSubLists.get(key) is None:
                anagramStringSubLists[key] = []
            anagramStringSubLists[key].append(item)
        # for key in anagramStringSubLists:
        return list(anagramStringSubLists.values())
        