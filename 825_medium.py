import collections


class Solution:
    def friendRequest(self, a, b):
        if b <= 0.5 * a + 7: return False
        if b > a: return False
        return True

    def numFriendRequests(self, ages) -> int:
        total = 0
        age_groups = collections.Counter(ages)
        for a, num_a in age_groups.items():
            for b, num_b in age_groups.items():
                if self.friendRequest(a, b):
                    total += num_a * num_b
                    if a == b: total -= num_a
        return total


if __name__ == "__main__":
    ages = [20, 30, 100, 110, 120]
    ages = [16, 16]
    ages = [16, 17, 18]
    ages = [101, 56, 69, 48, 30]
    sol = Solution()
    res = sol.numFriendRequests(ages)
    print(res)