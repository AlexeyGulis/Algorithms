class Solution:
    def checkValidString(self, s: str) -> bool:
        # dp = {}
        # def decision_tree(i, my_stack):
        #     if len(s) - i < len(my_stack):
        #         return False
        #     if i == len(s):
        #         if not my_stack:
        #             return True
        #         return False
        #     if s[i] == '(':
        #         temp = list(my_stack)
        #         temp.append(s[i])
        #         return decision_tree(i + 1, temp)
        #     if s[i] == ')':
        #         temp = list(my_stack)
        #         if temp:
        #             temp.pop()
        #             return decision_tree(i + 1, temp)
        #         else:
        #             return False
        #     if s[i] == '*':

        #         if (i, len(my_stack)) in dp:
        #             t1 = dp[(i, len(my_stack))]
        #         else:
        #             t1 = decision_tree(i + 1, my_stack)

        #         if (i, len(my_stack) - 1) in dp:
        #             t2 = dp[(i, len(my_stack) - 1)]
        #         else:
        #             temp = list(my_stack)
        #             t2 = False
        #             if temp:
        #                 temp.pop()
        #                 t2 = decision_tree(i + 1, temp)

        #         if (i, len(my_stack) + 1) in dp:
        #             t3 = dp[(i, len(my_stack) + 1)]
        #         else:
        #             temp = list(my_stack)
        #             temp.append('(')
        #             t3 = decision_tree(i + 1, temp)

        #         return t1 or t2 or t3


        # return decision_tree(0, [])
        left_min, left_max = 0, 0
        for i in range(len(s)):
            if s[i] == '(':
                left_max += 1
                left_min += 1
            if s[i] == ')':
                left_min = left_min - 1 if left_min - 1 >= 0 else 0
                if left_max - 1 < 0:
                    return False
                left_max -= 1
            if s[i] == '*':
                left_min = left_min - 1 if left_min - 1 >= 0 else 0
                left_max += 1
        if left_max == 0 or left_min == 0:
            return True
        return False


s = Solution()
print(s.checkValidString("(**(*()**()**((**(*)"))
