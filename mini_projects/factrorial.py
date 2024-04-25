def factorial(num):
    if num > 0:
        fac = num * factorial(num - 1)
        # 3 * 2 * 1 * 1
    else:
        return 1
    return fac

print(factorial(3))
