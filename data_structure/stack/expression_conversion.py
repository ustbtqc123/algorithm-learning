def expression_conversion(expression):
    expression_list = expression.split(" ")
    pref_dict = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
    output_list = []
    opt_chrs = [chr(i + ord('A')) for i in range(ord('Z') - ord('A')+1)]
    opt_nums = [str(i) for i in range(10)]
    opt_stack = []
    for token in expression_list:
        if token in opt_chrs or token in opt_nums:
            output_list.append(token)
        elif token == '(':
            opt_stack.append(token)
        elif token in "*/+-":
            if opt_stack:
                peek = opt_stack[-1]
                while pref_dict[token] <= pref_dict[peek] and opt_stack:
                    output_list.append(opt_stack.pop())
                    if opt_stack:
                        peek = opt_stack[-1]
            opt_stack.append(token)
        else:
            popped_val = opt_stack.pop()
            while popped_val != '(' and opt_stack:
                output_list.append(popped_val)
                popped_val = opt_stack.pop()

    while opt_stack:
        output_list.append(opt_stack.pop())

    return ''.join(output_list)


if __name__ == '__main__':
    test_expressions = [
        "A + B * C",
        "( A + B ) * C",
        "A * B + C * D",
        "1 + ( 5 * 6 + 4 ) * 8",
        "3 * 5 / 6 - 7 + 4"
    ]

    for test_expression in test_expressions:
        try:
            res = expression_conversion(test_expression)
            print(f"表达式: {test_expression}, 后缀表达式: {res}")
        except ValueError as e:
            print(f"表达式: {test_expression}, 错误: {e}")
