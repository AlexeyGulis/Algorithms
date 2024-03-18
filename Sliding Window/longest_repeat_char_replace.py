class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        answer = 0
        max_count = {}
        l = 0
        for i in range(len(s)):
            if s[i] not in max_count:
                max_count[s[i]] = 1
            else:
                max_count[s[i]] += 1
            if i - max(max_count.values()) - l + 1 <= k:
                if answer < i - l + 1:
                    answer = i - l + 1
            else:
                max_count[s[l]] -= 1
                l += 1
        return answer


s = Solution()
print(s.characterReplacement(
    s =
"ABAA",
    k=0))
