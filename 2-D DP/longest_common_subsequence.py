class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        two_d_array = [[0 for i in range(len(text2))] for i in range(len(text1))]
        for i in range(len(text1)):
            for j in range(len(text2)):
                t1 = 0
                t2 = 0
                t3 = 0
                if i != 0:
                    t1 = two_d_array[i - 1][j]
                if j != 0:
                    t2 = two_d_array[i][j - 1]
                if i != 0 and j != 0:
                    t3 = two_d_array[i - 1][j - 1]
                if text1[i] == text2[j]:
                    two_d_array[i][j] += t3 + 1
                else:
                    two_d_array[i][j] = max(t1, t2)

        return two_d_array[len(text1) - 1][len(text2) - 1]


s = Solution()
print(s.longestCommonSubsequence('ace', 'abcde'))
