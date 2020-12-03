def fe(n):
    if (n == 0) | (n == 1):
        return 1
    return fe(n - 1) + fe(n - 2)


n = int(input("输入：n="))
print("输出", fe(n))
