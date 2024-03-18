from typing import List


class Solution:
    n = 0
    m = 0

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        self.n = len(matrix)
        self.m = len(matrix[0])
        if matrix[0][0] > target or matrix[len(matrix) - 1][len(matrix[0]) - 1] < target:
            return False
        if matrix[self.n - 1][0] <= target:
            if self.binary(matrix[self.n - 1], target, 0, self.m - 1) == -1:
                return False
            else:
                return True
        else:
            return self.twoD_binary(matrix, target, 0, self.n - 1)

    def twoD_binary(self, matrix, target, col_left, col_right):
        if col_right - col_left == 1:
            if self.binary(matrix[col_left], target, 0, self.m - 1) != -1:
                return True
            else:
                return False
        if matrix[col_left + (col_right - col_left) // 2][0] == target:
            return True
        if matrix[col_left + (col_right - col_left) // 2][0] > target:
            return self.twoD_binary(matrix, target, col_left, col_left + (col_right - col_left) // 2)
        if matrix[col_left + (col_right - col_left) // 2][0] < target:
            return self.twoD_binary(matrix, target, col_left + (col_right - col_left) // 2, col_right)

    def binary(self, nums, target, left, right):
        ans = -1
        if abs(left - right) <= 1:
            if nums[right] == target:
                return right
            if nums[left] == target:
                return left
            return ans
        if nums[left + ((right - left) // 2)] == target:
            return left + ((right - left) // 2)
        if nums[left + ((right - left) // 2)] > target:
            return self.binary(nums, target, left, left + ((right - left) // 2))
        if nums[left + ((right - left) // 2)] < target:
            return self.binary(nums, target, left + ((right - left) // 2), right)


s = Solution()
print(s.searchMatrix(matrix=[[1],[3]], target=2))
