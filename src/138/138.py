
def rangeBitwiseAnd(a, b):
    ans = a
    if a+1 < b:
        for i in range(a+1, b):
            ans &= i
    return ans


if __name__ == "__main__":
    print(rangeBitwiseAnd(5, 7))  # 4
    print(rangeBitwiseAnd(0, 0))  # 0
    print(rangeBitwiseAnd(1, 2147483647))  # 0
