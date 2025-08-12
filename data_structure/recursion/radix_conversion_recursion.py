def radix_conversion_recursion(num, base):
    digits = "0123456789ABCDEF"
    if num < base:
        return digits[num]
    return radix_conversion_recursion(num // base, base) + digits[num % base]


if __name__ == '__main__':
    test_um = 5
    print(radix_conversion_recursion(test_um, 2))
