class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        my_d1 = {}
        if len(s1) > len(s2):
            return False
        for i in range(len(s1)):
            if s1[i] in my_d1:
                my_d1[s1[i]] += 1
            else:
                my_d1[s1[i]] = 1
        l = 0
        my_d2 = {}
        for i in range(len(s2)):
            if i - l + 1 > len(s1):
                my_d2[s2[l]] -= 1
                l += 1
            if s2[i] not in my_d2:
                my_d2[s2[i]] = 1
            else:
                my_d2[s2[i]] += 1
            check = True
            for k, v in my_d1.items():
                if k in my_d2:
                    if my_d2[k] != v:
                        check = False
                        break
                else:
                    check = False
                    break
            if check:
                return check

        return False


s = Solution()
print(s.checkInclusion('ab', 'cddabsdasdasdasdasd'))
