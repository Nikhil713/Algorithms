class Solution:
    def isValid(self, s: str) -> bool:
        checkParanthesis = []
        for i in s:
            if i == '(' or i =='[' or i == '{':
                checkParanthesis.append(i)
            if i == ')':
                if not checkParanthesis  or checkParanthesis[-1] != '(':
                    return False
                checkParanthesis.pop()
            if i == ']':
                if not checkParanthesis  or checkParanthesis[-1] != '[':
                    return False
                checkParanthesis.pop()
            if i == '}':
                if  not checkParanthesis  or checkParanthesis[-1] != '{':
                    return False
                checkParanthesis.pop()
        return not checkParanthesis
