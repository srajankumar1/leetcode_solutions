class Solution(object):
    def strStr(self, string, pattern):
        if not pattern:
            return 0

        for i in range(len(string) - len(pattern) + 1):
            j = 0
            while j < len(pattern) and string[i + j] == pattern[j]:
                j += 1
            if j == len(pattern):
                return i
        return -1