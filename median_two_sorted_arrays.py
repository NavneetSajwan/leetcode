class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        mid = len(nums)//2
        if len(nums)%2==0:
            return (nums[mid]+ nums[mid-1])/2
        else:
            return nums[mid]