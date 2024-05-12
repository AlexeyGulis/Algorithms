from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        my_dict = {}
        for val in hand:
            if val in my_dict:
                my_dict[val] += 1
            else:
                my_dict[val] = 1
        my_dict = dict(sorted(my_dict.items()))
        for i in range(len(hand) // groupSize):
            j = 0
            prev = None
            for k, v in my_dict.items():
                if j == groupSize:
                    break
                if my_dict[k] != 0:
                    if j == 0:
                        prev = k
                    else:
                        if k - prev > 1:
                            return False
                        prev = k
                    my_dict[k] -= 1
                    j += 1
            if j < groupSize:
                return False
        return True


s = Solution()
print(s.isNStraightHand(hand =
[8,10,12], groupSize = 3))
