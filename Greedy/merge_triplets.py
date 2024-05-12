from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        pointer = [False, False, False]
        for trplt in triplets:
            if trplt[0] == target[0]:
                if trplt[1] <= target[1] and trplt[2] <= target[2]:
                    pointer[0] = True
            if trplt[1] == target[1]:
                if trplt[0] <= target[0] and trplt[2] <= target[2]:
                    pointer[1] = True
            if trplt[2] == target[2]:
                if trplt[0] <= target[0] and trplt[1] <= target[1]:
                    pointer[2] = True
        return True if pointer[0] and pointer[1] and pointer[2] else False


s = Solution()
print(s.mergeTriplets(triplets = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]], target = [5,5,5]))
