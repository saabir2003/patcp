class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #nums1=nums[::-1]
        if target not in nums:
            return [-1,-1]
        sind=nums.index(target)
        eind=len(nums[::-1])-nums[::-1].index(target)-1
        return[sind,eind]
        