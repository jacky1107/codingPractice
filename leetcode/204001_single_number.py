class Solution:
    def singleNumber(self, nums):
        hashTable = {}
        for i, num in enumerate(nums):
            if str(num) in hashTable:
                hashTable[str(num)] = 2
            else:
                hashTable[str(num)] = 1
        result = [k for k, v in hashTable.items() if v == 1]
        return int(result[0]) if len(result) != 0 else None

nums = [4,1,2,1,2]
sol = Solution()
num = sol.singleNumber(nums)
print(num)