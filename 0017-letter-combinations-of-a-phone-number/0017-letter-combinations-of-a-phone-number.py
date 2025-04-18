class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def checker(n):
            my_dictionary={'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
            start=[]
            if len(n)!=0:
                n=list(n)
                n=[my_dictionary[i] for i in n]
                start=list(n[0])
                for i in range(1,len(n)):
                    b=[]
                    for j in start:
                        for k in n[i]:
                            b.append(j+k)
                    start=b
            return start
        return checker(digits)
            