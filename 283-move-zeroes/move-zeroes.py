class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i=0
        while True:
            j=nums.count(0)
        #print(j)
            if i!=j:
                nums.remove(0)
                nums.append(0)
            #print(nums)
                i=i+1
            else:
                return nums
        