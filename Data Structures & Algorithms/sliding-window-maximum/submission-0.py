class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        print(len(dq))
        maxElementIndexInWindow = list()
        for i in range(0, len(nums), 1):
            while(len(dq) != 0 and nums[dq[-1]] <= nums[i]):
                dq.pop()
            dq.append(i)
            if i >= k-1:
                while(len(dq) != 0 and dq[0] <= i-k):
                    dq.popleft()
                maxElementIndexInWindow.append(dq[0])
        maxElementInWindow = list()
        for i in maxElementIndexInWindow:
            maxElementInWindow.append(nums[i])
        return maxElementInWindow
