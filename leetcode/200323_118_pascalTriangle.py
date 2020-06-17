class Solution:
    def generate(self, numRows: int):
        if numRows == 0: return []
        if numRows == 1: return [[1]]
        res = [
            [1],
            [1,1]
        ]
        i = 1
        while i < numRows - 1:
            j = 0
            t = j + 1
            temp = [1]
            while t <= (len(res[i]) - 1):
                s = res[i][j] + res[i][t]
                temp.append(s)
                j += 1
                t = j + 1
            temp.append(1)
            res.append(temp)
            i += 1
        return res

numRows = 6
sol = Solution()
res = sol.generate(numRows)
print(res)