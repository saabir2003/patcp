class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num=x
        num=str(num)
        r=num[::-1]
        if r[-1]=="-":
            r=r[0:-1]
            r=int(r)
            r=-r
        r=int(r)
        if r >= -(2**31) and r <= (2**31)-1:
            return r
        else :
            return 0
        