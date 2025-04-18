class Solution:
    def countAndSay(self, n: int) -> str:
        def compartmentalize(initial):
            one="-"
            last="-"
            collector=""
            initial=initial+"-"
            for i in initial:

                if last==i:
                    one=one+i

                elif i=="-":
                    collector=collector+(str(len(one))+last)  
                else:

                    collector=collector+(str(len(one))+last)
                    last=i
                    one=i
            return(collector[2:])
        print(compartmentalize("1"))
        k="1"
        if n==1:
            return "1"
        else:
            n=n-1
            for i in range(n):
                k=compartmentalize(k)
            return k