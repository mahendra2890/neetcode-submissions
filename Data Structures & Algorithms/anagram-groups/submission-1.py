class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create dict: sorted(anagram), [values] -> create array of [values per anagram] -> return
        anagramStringSubLists = defaultdict(lambda: [])
        for item in strs:
            key = "".join(sorted(item))
            anagramStringSubLists[key].append(item)
        # for key in anagramStringSubLists:
        return list(anagramStringSubLists.values())
        