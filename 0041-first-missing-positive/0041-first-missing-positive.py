class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums=set(nums)
        i=1
        while i>0:
            if i not in nums:
                return i
            i=i+1
                