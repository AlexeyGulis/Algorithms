from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        ans = []
        for num in nums:
            if num not in my_dict:
                my_dict[num] = 1
            else:
                my_dict[num] += 1
        r = 0
        for num, val in sorted(my_dict.items(), key=lambda x: x[1], reverse=True):
            if r < k:
                ans.append(num)
                r += 1
            else:
                return ans

        return ans


s = Solution()
print(s.topKFrequent(nums=[1, 1, 1, 2, 2, 3, 3], k=2))
