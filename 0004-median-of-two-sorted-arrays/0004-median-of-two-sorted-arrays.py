class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n=nums1+nums2
        n=sorted(n)
        print(n)
        e=len(n)
        y=int(e/2)
        if e%2==0:
            t=float((n[y-1]+n[y])/2)
        else:
            o=int((e-1)/2)
            t=float(n[o])
        return t