from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        i = 0
        j = len(height) - 1
        while j - i >= 1:
            if height[i] <= height[j]:
                ans = max(ans, min(height[i], height[j]) * (j - i))
                i += 1
            else:
                ans = max(ans, min(height[i], height[j]) * (j - i))
                j -= 1
        return ans


s = Solution()
print(s.maxArea(height=[1, 2, 4, 3]))
