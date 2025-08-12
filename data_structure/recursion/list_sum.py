def list_sum_recursion(input_list):
    if len(input_list) == 1:
        return input_list[0]

    return input_list[0] + list_sum_recursion(input_list[1:])


if __name__ == '__main__':
    test_list = [1, 2, 3, 4, 5, 50]
    print(list_sum_recursion(test_list))
