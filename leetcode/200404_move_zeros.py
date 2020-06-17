class Solution:
    def moveZeroes(self, nums):
        i = 0
        pointer = len(nums)
        while i < len(nums):
            if pointer < i and nums[i] != 0:
                temp = nums[i]
                nums[i] = nums[pointer]
                nums[pointer] = temp
                i = pointer + 1
                pointer = len(nums)
            if nums[i] == 0:
                pointer = min(pointer, i)
            i += 1
        return nums

nums = [0,1,0,0,1,2,10,3,12,0]
sol = Solution()
nums = sol.moveZeroes(nums)
print(nums)