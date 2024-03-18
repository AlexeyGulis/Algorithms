from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        sec_slow = 0
        while True:
            slow = nums[slow]
            sec_slow = nums[sec_slow]
            if slow == sec_slow:
                return slow


s = Solution()

print(s.findDuplicate([]))
