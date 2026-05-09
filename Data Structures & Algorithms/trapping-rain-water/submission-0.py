class Solution:
    def trap(self, height: List[int]) -> int:
        # Arr: [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
        # NGE: [1, 3, 3, 7, 7, 7, 7,10,10,10]
        # PGE: [-1,-1,1, 1, 3, 3, 3, 3, 7, 8]
        # ans+=[0, 0, 2, 0, 2, 3, 2, 0, 0, 0]
        NGE = [len(height)-1]*len(height)
        PGE = [0]*len(height)
        for i in range(0, len(height), 1):
            if i == 0 or height[i] >= height[PGE[i-1]]:
                PGE[i] = i
            else:
                PGE[i] = PGE[i-1]
        
        for i in range(len(height)-1, 0, -1):
            if i == len(height)-1 or height[i] >= height[NGE[i+1]]:
                NGE[i] = i
            else:
                NGE[i] = NGE[i+1]
        ans = 0
        print(height)
        print(NGE)
        print(PGE)
        for i in range(0, len(height), 1):
            ans+=(max(0, min(height[PGE[i]], height[NGE[i]])-height[i]))
        return ans

        