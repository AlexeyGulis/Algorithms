from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        list_copy = strs.copy()
        for i in range(len(list_copy)):
            list_copy[i] = ''.join(sorted(list_copy[i]))
        my_dict = {}
        for i in range(len(list_copy)):
            if list_copy[i] not in my_dict:
                my_dict[list_copy[i]] = [strs[i]]
            else:
                my_dict[list_copy[i]].append(strs[i])

        ans = []
        for key, val in my_dict.items():
            ans.append(val)
        return ans


s = Solution()

print(s.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
