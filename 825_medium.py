class Solution:
    def numFriendRequests(self, ages) -> int:
        res, point = 0, len(ages)
        ages = sorted(ages)

        for i in range(len(ages)):
            if ages[i] >= 100:
                point = i
                break

        a, b = ages[:point], ages[point:]
        a = a[::-1]
        b = b[::-1]
        res_a = self.find_request(a)
        res_b = self.find_request(b)
        return res_a + res_b

    def find_request(self, ages):
        res = 0
        for i in range(len(ages) - 1):
            for j in range(i + 1, len(ages)):
                if not self.condition(ages[i], ages[j]):
                    res += 1
                if not self.condition(ages[j], ages[i]):
                    res += 1
        return res

    def condition(self, a, b):
        return b <= 0.5 * a + 7


if __name__ == "__main__":
    ages = [16, 17, 18]
    ages = [20, 30, 100, 110, 120]
    ages = [16, 16]
    sol = Solution()
    res = sol.numFriendRequests(ages)
    print(res)