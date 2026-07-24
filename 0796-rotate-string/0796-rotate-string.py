class Solution(object):
    def rotateString(self, s, goal):
        if len(s) != len(goal):
            return False
        con=s+s
        if goal in con:
            return True
        else:
            return False