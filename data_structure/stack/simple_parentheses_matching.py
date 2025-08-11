def parentheses_matching(_test_str):
    stack = []
    for char in _test_str:
        if char in "([{":
            stack.append(char)
        else:
            if not stack:
                return False
            left = stack.pop()
            if not matches(left, char):
                return False
    if not stack:
        return True
    else:
        return False


def matches(left, right):
    left_list = ['{', '[', '(']
    right_list = ['}', ']', ')']
    return left_list.index(left) == right_list.index(right)


if __name__ == '__main__':
    test_str1 = "((()))"
    test_str2 = "((())()()()[][][]"
    test_str3 = "([{}])"
    test_str4 = "([)]"

    res1 = parentheses_matching(test_str1)
    res2 = parentheses_matching(test_str2)
    res3 = parentheses_matching(test_str3)
    res4 = parentheses_matching(test_str4)

    print(f"测试字符串 {test_str1} 的结果: {res1}")
    print(f"测试字符串 {test_str2} 的结果: {res2}")
    print(f"测试字符串 {test_str3} 的结果: {res3}")
    print(f"测试字符串 {test_str4} 的结果: {res4}")
