class Solution:
    def check(self, res, target, num, nums, i):
        for n in target:
            if i not in n:
                a = nums[n[0]]
                b = nums[n[1]]
                s = num + a + b
                if s == 0:
                    lst = sorted([num, a, b])
                    if lst not in res: res.append(lst)
        return res

    def threeSum(self, nums):
        dic = {}
        res = []
        neg, mid, pos = [], [], []
        if len(nums) < 3: return res
        for i, num in enumerate(nums):
            for j in range(i+1,len(nums)):
                index = [i,j]
                s = num + nums[j]
                if s < 0: neg.append(index)
                elif s > 0: pos.append(index)
                else: mid.append(index)
        for i, num in enumerate(nums):
            if num > 0:
                res = self.check(res, neg, num, nums, i)
            elif num < 0:
                res = self.check(res, pos, num, nums, i)
            else:
                res = self.check(res, mid, num, nums, i)
        return res
# [0,0,0,0]
# [-1,0,1,0]
# [-2,0,1,1,2]
# [-1,0,1,2,-1,-4]
# [9,8,7,3,9,-3,9,1,5,-5,-2,5]
# nums = [-1,0,1,2,-1,-4,-12,-12,9,3,-14,-2,-5,-6,7,8,2,-4,6,-5,-10,-4,-9,-14,-14,12,-13,-7,3,7,2,11,7,9,-4,13,-6,-1,-14,-12,9,9,-6,-11,10,-14,13,-2,-11,-4,8,-6,0,7,-12,1,4,12,9,14,-4,-3,11,10,-9,-8,8,0,-1,1,3,-15,-12,4,12,13,6,10,-4,10,13,12,12,-2,4,7,7,-15,-4,1,-15,8,5,3,3,11,2,-11,-12,-14,5,-1,9,0,-12,6,-1,1,1,2,-3]#, 0, 1, 2, -1, -4]

# nums = [9,8,7,3,9,-3,9,1,5,-5,-2,5,0,0,0]
# nums = [-1,0,1,2,-1,-4]
sol = Solution()
res = sol.threeSum(nums)
print(res)
