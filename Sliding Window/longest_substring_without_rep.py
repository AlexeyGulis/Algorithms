class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        my_dict = {}
        left = 0
        right = 0
        for i in range(len(s)):
            if i == 0:
                my_dict[s[i]] = i
                left = 0
                right = 1
            else:
                if s[i] in my_dict:
                    if answer < right - left:
                        answer = right - left
                    if left <= my_dict[s[i]]:
                        left = my_dict[s[i]] + 1
                        my_dict[s[i]] = i
                        right += 1
                    else:
                        my_dict[s[i]] = i
                        right += 1
                else:
                    my_dict[s[i]] = i
                    right += 1
        if answer < right - left:
            answer = right - left
        return answer


s = Solution()
print(s.lengthOfLongestSubstring("abba"))
