class SegmentTree:
    def __init__(self, N, A):
        self.n = N
        while (self.n & (self.n - 1)) != 0:
            # complete binary tree - only the last row(leaves) can be incomplete.
            # since we need all items from the arr in last row(leaves) - we need the last row to have atleast len(nums) spots. Since the last row will be children of second last row = so it's size will be 2^something, so we keep on increasing size till we get 2^something 
            self.n += 1
        self.build(N, A)

    def build(self, N, A):
        self.tree = [float('-inf')] * (2 * self.n)
        # 2*self.n because last row contains the actual elements, and everything before that is some subtree's root node
        for i in range(N):
            self.tree[self.n + i] = A[i]
        for i in range(self.n - 1, 0, -1):
            #2*i, and 2*i+1; not 2*i+1, and 2*i+2 because the tree is 1-indexed. 
            # If we wanted to make it 0-indexed it would be (2*self.n-1) size 
            # and array elements will be populated from [self.n-1, ..., self.n+N-2] instead of [self.n, ..., self.n+N-1]
            self.tree[i] = max(self.tree[2*i], self.tree[2*i+1])

    def query(self, l, r):
        res = float('-inf')
        l += self.n
        r += self.n + 1
        # r is not included
        while l < r:
            if l & 1:
                # l is odd means this is a right child of some other node 
                # so this needs to be considered because its parent can't be
                res = max(res, self.tree[l])
                l += 1
                # root of l can't be condidered, but l+1 will be: because l is odd, so l and l+1's roots are different
            if r & 1:
                # r is odd means (r-1) is even: which means (r-1) is left child of its parent
                # so the parent can't be considered but r-1 needs to be
                res = max(res, self.tree[r-1])
                # r/2 is parent of the subtree r-1 is part of, and (r-1)/2 is that-1 so in range
                r -= 1
            l >>= 1
            r >>= 1
        return res


class Solution:
    def maxSlidingWindow(self, nums, k):
        n = len(nums)
        segTree = SegmentTree(n, nums)
        output = []
        for i in range(n - k + 1):
            output.append(segTree.query(i, i + k - 1))
        return output