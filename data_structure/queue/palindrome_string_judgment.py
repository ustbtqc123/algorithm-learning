from collections import deque


def palindrome_string_judgment(input_str):
    deque_str = deque()
    for char in input_str:
        deque_str.append(char)
    while len(deque_str) > 1:
        left_char = deque_str.popleft()
        right_char = deque_str.pop()
        if left_char != right_char:
            return False
    return True


if __name__ == '__main__':
    test_str1 = "man"
    test_str2 = "mam"
    test_str3 = "baab"
    print(palindrome_string_judgment(test_str1))
    print(palindrome_string_judgment(test_str2))
    print(palindrome_string_judgment(test_str3))

