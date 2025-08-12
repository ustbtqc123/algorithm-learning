def expression_calculate(postfix_str):
    opt_nums = [str(i) for i in range(10)]
    opt_stack = []
    postfix_list = postfix_str.split(' ')
    for token in postfix_list:
        if token in opt_nums:
            opt_stack.append(int(token))
        else:
            right_num = opt_stack.pop()
            left_num = opt_stack.pop()
            opt_stack.append(calculate(left_num, right_num, token))
    return opt_stack.pop()


def calculate(a, b, cal_chr):
    if cal_chr == '*':
        return a * b
    elif cal_chr == '/':
        return a / b
    elif cal_chr == '+':
        return a + b
    elif cal_chr == '-':
        return a - b


if __name__ == '__main__':
    test_postfix_str = "1 5 6 * 4 + 8 * +"
    res = expression_calculate(test_postfix_str)
    print(res)
