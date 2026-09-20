class Solution:
    def twoSum(self,nums,target):
        for i,num in enumerate(nums):
            complement=target-num
            for m in range(i+1,len(nums)):
                    if nums[m]==complement:
                        pass
                        return [i,m]
s=Solution()
nums=list(map(int,input("ENTER THE NUMBERS").split())) 
target=int(input("ENTER THE TARGET"))
o=s.twoSum(nums,target)   
print(o)