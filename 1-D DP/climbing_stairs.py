class Solution:
    answer = 0
    def climbStairs(self, n: int) -> int:
        self.answer = 0
        my_sum = [1, 2]
        for i in range(n):
            if i == 0:
                self.answer = my_sum[0]
            if i == 1:
                self.answer = my_sum[1]
            if i > 1:
                temp = my_sum[0] + my_sum[1]
                self.answer = temp
                my_sum[0] = my_sum[1]
                my_sum[1] = temp

        return self.answer


s = Solution()
print(s.climbStairs(38))
