class Solution(object):
    def lengthOfLongestSubstring(self, s):
        hi=0
        arr=[]
        l=list(s)
        for i in range(0,len(l)):
            a=l[i]
            
            if a not in arr:
                arr.append(a)
                ho=len(arr)
                if ho > hi:
                    hi=ho
            else:
                ind=arr.index(a)
                
                arr=arr[ind+1:]
                arr.append(a)
        
        return hi
        
        