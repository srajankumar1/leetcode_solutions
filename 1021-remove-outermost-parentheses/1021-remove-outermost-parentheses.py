class Solution(object):
    def removeOuterParentheses(self, s):
        level=0
        result=""
        for char in s:
            if char=="(":
                if level>0:
                    result+=char
                level+=1
            if char==")":
                level-=1
                if level>0:
                    result+=char
        return result