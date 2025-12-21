class Solution:
    def minWindow(self, s, t):
        if not s or not t:
            return ""

        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        required = len(need)
        formed = 0
        window = {}

        l = 0
        ans = (float("inf"), 0, 0)

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in need and window[c] == need[c]:
                formed += 1

            while l <= r and formed == required:
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                ch = s[l]
                window[ch] -= 1
                if ch in need and window[ch] < need[ch]:
                    formed -= 1
                l += 1

        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]