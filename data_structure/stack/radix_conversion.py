def radix_conversion(num, radix):
    if num == 0:
        return "0"
    stack = []
    digits = "0123456789ABCDEF"
    while num != 0:
        left = num % radix
        stack.append(left)
        num = num // radix
    res_str = ""
    while stack:
        popped_index = stack.pop()
        res_str += digits[popped_index]
    return res_str


if __name__ == '__main__':
    test_num = 5
    radix_2 = radix_conversion(test_num, 2)
    # radix_8 = radix_conversion(test_num, 8)
    # radix_16 = radix_conversion(test_num, 16)
    print(f"十进制数 {test_num} 转换为二进制是: {radix_2}")
    # print(f"十进制数 {test_num} 转换为八进制是: {radix_8}")
    # print(f"十进制数 {test_num} 转换为十六进制是: {radix_16}")
