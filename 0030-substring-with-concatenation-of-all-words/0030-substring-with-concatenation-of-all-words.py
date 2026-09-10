class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_len=len(words[0])
        word_count=len(words)
        total_len=word_len*word_count

        if total_len>len(s):
            return []

        freq={}
        for word in words:
            freq[word]=freq.get(word,0)+1

        ans=[]

        for start in range(word_len):
            left=start
            count=0
            seen={}

            for right in range(start,len(s)-word_len+1,word_len):
                word=s[right:right+word_len]

                if word not in freq:
                    seen={}
                    count=0
                    left=right+word_len
                    continue

                seen[word]=seen.get(word,0)+1
                count+=1

                while seen[word]>freq[word]:
                    left_word=s[left:left+word_len]
                    seen[left_word]-=1
                    left+=word_len
                    count-=1

                if count==word_count:
                    ans.append(left)

        return ans