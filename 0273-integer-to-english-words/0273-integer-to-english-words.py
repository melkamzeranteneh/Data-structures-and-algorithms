class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                    "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]
        
        def helper(n):
            if n == 0:
                return ""
            elif n < 20:
                return below_20[n] + " "
            elif n < 100:
                return tens[n // 10] + " " + helper(n % 10)
            else:
                return below_20[n // 100] + " Hundred " + helper(n % 100)
        
        res = ""
        for i in range(len(thousands)):
            if num % 1000 != 0:
                res = helper(num % 1000) + thousands[i] + " " + res
            num //= 1000
        
        return res.strip()
        #def count(n):
            #d={0:"zero",1:"One",2:"Two",3:"Three",4:"four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",10:"Ten",11:"Eleven",12:"Twelve",13:"Thirteen",14:"Fourteen",15:"Fifteen",16:"Sixteen",17:"Seventen",18:"Eighteen",19:"Nineteen",20:"Twenty",30:"Thirty",40:"Fourty",50:"Fifty",60:"Sixty",70:"Seventy",80:"Eighty",90:"Ninety"}
