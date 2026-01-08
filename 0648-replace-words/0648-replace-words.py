class Solution:
    def replaceWords(self, dictionary, sentence):
        trie={}
        for w in dictionary:
            cur=trie
            for c in w:
                if c not in cur:
                    cur[c]={}
                cur=cur[c]
            cur["#"]=True
        def root(word):
            cur=trie
            pref=""
            for c in word:
                if "#" in cur or c not in cur:
                    break
                cur=cur[c]
                pref+=c
            return pref if "#" in cur else word
        res=[]
        for w in sentence.split():
            res.append(root(w))
        return " ".join(res)