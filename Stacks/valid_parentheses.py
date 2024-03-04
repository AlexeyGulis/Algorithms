import queue


class Solution:
    def isValid(self, s: str) -> bool:
        q1 = queue.LifoQueue()
        my_list = list(s)
        for l in my_list:
            if l == '(' or l == '[' or l == '{':
                q1.put(l)
            if l == ')' or l == ']' or l == '}':
                if q1.empty():
                    return False
                r = q1.get()
                if r == '(':
                    if l != ')':
                        return False
                elif r == '[':
                    if l != ']':
                        return False
                elif r == '{':
                    if l != '}':
                        return False
        if not q1.empty():
            return False
        return True


s = Solution()
print(s.isValid(s =
"("))
