class Solution(object):
    def compress(self, chars):
        count=1
        s=[]

        s.append(chars[0])

        for i in range(1,len(chars)):
            if chars[i-1]!=chars[i]:
                if count>1:
                    for digit in str(count):
                        s.append(digit)

                s.append(chars[i])
                count=1
            else:
                count+=1

        if count>1:
            for digit in str(count):
                s.append(digit)

        for i in range(len(s)):
            chars[i]=s[i]

        return len(s)