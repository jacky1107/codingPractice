class Solution:
    def maxSubArray(self, nums) -> int:
        localNum = nums[0]
        globalNum = nums[0]
        for num in nums[1:]:
            localNum = max( num, num + localNum )
            globalNum = max( localNum, globalNum )
        return globalNum

            
nums = [-2,1,-3,4,-1,2,1,-5]#,4,3,3,3,3,3]
sol = Solution()
num = sol.maxSubArray(nums)
print(num)