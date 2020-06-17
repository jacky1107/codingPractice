class Solution:
    def groupAnagrams(self, strs):
        result = {}
        for s in strs:
            temp = ''.join(sorted(s))
            if temp not in result:
                result[temp] = [s]
            else:
                lst = result[temp]
                lst.append(s)
                result[temp] = lst
        return list(result.values())

nums = ["eat", "tea", "tan", "ate", "nat", "bat"]
nums = ["cab","tin","pew","duh","may","ill","buy","bar","max","doc"]
sol = Solution()
nums = sol.groupAnagrams(nums)
print(nums)