
class Solution:
    result = False
    def checkValidString(self, s: str) -> bool:
        def help(i, my_stack):
            if self.result:
                return
            if i == len(s):
                if not my_stack:
                    self.result = True
                return
            if s[i] == '(':
                temp = list(my_stack)
                temp.append(s[i])
                help(i + 1, temp)
            if s[i] == ')':
                temp = list(my_stack)
                if temp:
                    temp.pop()
                    help(i + 1, temp)
                else:
                    return
            if s[i] == '*':

                help(i + 1, my_stack)

                temp = list(my_stack)
                if temp:
                    temp.pop()
                    help(i + 1, temp)

                temp = list(my_stack)
                temp.append('(')
                help(i + 1, temp)

        help(0, [])


        return self.result


s = Solution()
print(s.checkValidString("(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"))
