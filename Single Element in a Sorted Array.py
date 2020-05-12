You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.



class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start=0
        end=len(nums)-1
        mid=(start+end)//2
        if(len(nums)==1):
            return nums[0]
        if(mid%2==0):
            if(nums[mid]==nums[mid-1]):
                for i in range (0,mid-1,2):
                    if(nums[i]!=nums[i+1]):
                        return nums[i] 
            elif(nums[mid]==nums[mid+1]):
                for i in range (len(nums)-1,mid+1,-2):
                    if(nums[i]!=nums[i-1]):
                        return nums[i]
            else:
                return nums[mid]
        else:
            if(nums[mid]==nums[mid+1]):
                for i in range (0,mid-2,2):
                    if(nums[i]!=nums[i+1]):
                        return nums[i]
                return nums[mid-1]
            elif(nums[mid]==nums[mid-1]):
                for i in range (len(nums)-1,mid+2,-2):
                    if(nums[i]!=nums[i-1]):
                        return nums[i]
                return nums[mid+1]
            else:
                return nums[mid]
      
