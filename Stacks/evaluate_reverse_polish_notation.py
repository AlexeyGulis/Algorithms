from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        my_list = []
        my_str = ''
        for tok in tokens:
            if tok == '+':
                q1 = my_list.pop()
                q2 = my_list.pop()
                my_list.append(q1 + q2)
            elif tok == '-':
                q1 = my_list.pop()
                q2 = my_list.pop()
                my_list.append(q2 - q1)
            elif tok == '*':
                q1 = my_list.pop()
                q2 = my_list.pop()
                my_list.append(q1 * q2)
            elif tok == '/':
                q1 = my_list.pop()
                q2 = my_list.pop()
                my_list.append(-(abs(q2) // abs(q1)) if q2 // q1 < 0 else q2 // q1)
            else:
                my_list.append(int(tok))
        return my_list[0]


s = Solution()
print(s.evalRPN(
    ["-78", "-33", "196", "+", "-19", "-", "115", "+", "-", "-99", "/", "-18", "8", "*", "-86", "-", "-", "16", "/",
     "26", "-14", "-", "-", "47", "-", "101", "-", "163", "*", "143", "-", "0", "-", "171", "+", "120", "*", "-60", "+",
     "156", "/", "173", "/", "-24", "11", "+", "21", "/", "*", "44", "*", "180", "70", "-40", "-", "*", "86", "132",
     "-84", "+", "*", "-", "38", "/", "/", "21", "28", "/", "+", "83", "/", "-31", "156", "-", "+", "28", "/", "95",
     "-", "120", "+", "8", "*", "90", "-", "-94", "*", "-73", "/", "-62", "/", "93", "*", "196", "-", "-59", "+", "187",
     "-", "143", "/", "-79", "-89", "+", "-"]))
