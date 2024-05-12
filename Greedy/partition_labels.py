from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        my_dict = {}
        my_sec_dict = {}
        j = 0
        for i in range(len(s)):
            if s[i] in my_dict:
                j = my_dict[s[i]]
                for k in range(my_sec_dict[s[i]], i):
                    my_dict[s[k]] = j
                my_sec_dict[s[i]] = i
            else:
                my_dict[s[i]] = j + 1
                my_sec_dict[s[i]] = i
                j += 1
        res = [0 for i in range(max(my_dict.values()))]
        for c in s:
            res[my_dict[c] - 1] += 1

        return res


s = Solution()
print(s.partitionLabels(s = "eccbbbbdec"))

