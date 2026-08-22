class Solution(object):
    def removeDuplicateLetters(self, s):
        # Store the last occurrence of each character
        last_index = {}

        for i in range(len(s)):
            last_index[s[i]] = i

        stack = []
        present = set()

        for i in range(len(s)):
            ch = s[i]

            if ch in present:
                continue

            # Remove characters that are larger than ch
            # and appear again later
            while (stack and
                   stack[-1] > ch and
                   last_index[stack[-1]] > i):

                removed = stack.pop()
                present.remove(removed)

            stack.append(ch)
            present.add(ch)

        return "".join(stack)