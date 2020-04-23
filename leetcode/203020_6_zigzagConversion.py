class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = ""
        step = 2 * (numRows - 1)
        if step == 0: return s
        i, r = 0, 0
        while len(result) != len(s):
            if i >= len(s):
                r += 1
                j = 1
                i = r
            stepA = step - 2 * r
            stepB = (step - stepA)
            result += s[i]
            if r == 0 or r == (numRows - 1):
                i += step
            else:
                if j == 1:
                    i += stepA
                    j -= 1
                else:
                    i += stepB
                    j += 1
        return result

s = "ABCDEF" # "PAYPALISHIRING"
numRows = 3
sol = Solution()
result = sol.convert(s, numRows)
print(result)
