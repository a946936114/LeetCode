class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        water = 0
        n = len(height)
        for y in range(1, max(height)+1):
            for i in range(0, n):
                # 墙比当前层数高
                if height[i] >= y:
                    i1 = i
                    break
            for i in range(n - 1, -1, -1):
                # 墙比当前层数高
                if height[i] >= y:
                    i2 = i
                    break
            if i1 != i2:
                for i in range(i1, i2 + 1):
                    if height[i] < y:
                        water = water + 1

        return water
