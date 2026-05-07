class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(lambda: 0)
        for item in nums:
            frequency[item]+=1
        return [item[0] for item in sorted(frequency.items(), key=lambda item: item[1], reverse = True)[:k]]