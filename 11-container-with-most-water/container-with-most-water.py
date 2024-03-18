class Solution(object):
    def maxArea(self,height):
        i=0
        j=len(height)-1
        a=0
        while j>=i:
            x=j-i
            y=min(height[i],height[j])
            ar=x*y
            if ar > a :
                a=ar
            if height[i] > height[j]:
                j=j-1
            else:
                i=i+1
        return a
        