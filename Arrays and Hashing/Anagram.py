class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        dict_s = {}
        for let in s:
            if let not in dict_s:
                dict_s[let] = 1
            else:
                dict_s[let] += 1

        for let in t:
            if let in dict_s:
                if dict_s[let] == 0:
                    return False
                else:
                    dict_s[let] -= 1
            else:
                return False

        return True


s = Solution()

print(Solution.isAnagram(s, "ab", "a"))
