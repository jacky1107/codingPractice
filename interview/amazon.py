class Solution:
    def rotationByMath(self, lst):
        n = len(lst)
        new = []
        for i in range(n):
            temp = []
            for j in range(n):
                temp.append(0)
            new.append(temp)
        for i in range(n):
            for j in range(n):
                c = n - i - 1
                new[j][c] = lst[i][j]
        return new

    def rotationByMethod(self, lst):
        n = len(lst)
        for i in range(n):
            for j in range(i, n):
                # transpose
                temp = lst[i][j]
                lst[i][j] = lst[j][i]
                lst[j][i] = temp
        for i in range(n):
            for j in range(int(n/2)):
                # horizontally
                temp = lst[i][j]
                lst[i][j] = lst[i][n-j-1]
                lst[i][n-j-1] = temp
        return lst

lst = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 10, 11],
    [12, 13, 14, 15]]

lst = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]]

lst = [
    [0, 1, 2, 3, 4],
    [5, 6, 7, 8, 9],
    [10, 11, 12, 13, 14],
    [15, 16, 17, 18, 19],
    [20, 21, 22, 23, 24]]

sol = Solution()
math = sol.rotationByMath(lst)
method = sol.rotationByMethod(lst)
print(math)
print(method)
