class Solution:
    def findKthPositive(self, arr, k):
        i = 1
        j = 0
        index = 0
        while index < k:
            if i < arr[j]:
                i += 1
                index += 1
            elif i == arr[j]:
                i += 1
                if j < len(arr) - 1:
                    j += 1
            else:
                i += 1
                index += 1
        return i - 1


s = Solution()
index = s.findKthPositive([1, 2, 3, 4], 2)
print(index)
