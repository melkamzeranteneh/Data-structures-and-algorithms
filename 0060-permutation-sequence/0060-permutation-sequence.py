class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def per(s,k=0,n=0):
            if len(s)<2:
                return s
            p=[]
            for i in range(len(s)):
                x=s[i]
                xl=s[:i]+s[i+1:]
                for b in per(xl):
                    if len(s)==n and len(p)==k:
                        break
                    p.append(x+b)
                if len(s)==n and len(p)==k:
                    break
            if len(s)==n and len(p)==k:
                return p[-1]
            return p
        s="01234567890"
        s=s[1:n+1]
        return per(s,k,n)
