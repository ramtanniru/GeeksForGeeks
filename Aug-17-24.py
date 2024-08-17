class Solution:
    def productExceptSelf(self, nums):
        pr = 1
        zero = 0
        for i in nums:
            if i!=0:
                pr *= i
            else:
                zero += 1
        
        for i in range(len(nums)):
            if nums[i]!=0:
                if zero==0:
                    nums[i] = pr//nums[i]
                else:
                    nums[i] = 0
            else:
                if zero>1:
                    nums[i] = 0
                else:
                    nums[i] = pr 
        return nums 