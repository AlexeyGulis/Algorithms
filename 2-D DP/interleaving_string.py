class Solution:

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        self.res = False
        dp = {}

        def decisionTree(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if i + j >= len(s3):
                if i == len(s1) and j == len(s2):
                    return True
                return False
            t1, t2 = False, False
            if i < len(s1) and s1[i] == s3[i + j]:
                t1 = decisionTree(i + 1, j)
            if j < len(s2) and s2[j] == s3[i + j]:
                t2 = decisionTree(i, j + 1)
            dp[i, j] = t1 or t2
            return t1 or t2

        dp[(0, 0)] = decisionTree(0, 0)

        return dp[(0,0)]


s = Solution()
print(s.isInterleave(s1 = "a", s2 = "b", s3 = "a"))

my_s = 'aaDssS'
print(sum([1 if my_s[i].isupper() else 0 for i in range(len(my_s))]))
