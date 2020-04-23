class Solution:
    def countElements(self, arr):
        count = 0
        temp = []
        arr = sorted(arr)
        for i in range(len(arr)):
            temp.append(arr[i] + 1)
            if arr[i] in temp:
                count += 1
            print(temp, arr[i])
        return count


nums = [1, 3, 2, 3, 5, 0]
nums = [1,1,3,3,5,5,7,7] 
sol = Solution()
nums = sol.countElements(nums)
print(nums)
