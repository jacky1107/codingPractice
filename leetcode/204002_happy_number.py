class Solution:
    def isHappy(self, n: int) -> bool:
        firstNum = []
        while True:
            n =  str(n)
            s = 0
            for i in range(len(n)):
                s += int(n[i])**2
            n = s
            if n in firstNum: return False
            elif n == 1: return True
            firstNum.append(n)

n = 19
sol = Solution()
num = sol.isHappy(n)
print(num)