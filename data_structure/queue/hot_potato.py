from collections import deque


def hot_potato(name_list, num):
    queue = deque(name_list)
    while len(queue) > 1:
        for i in range(num):
            queue.append(queue.popleft())
        queue.popleft()
    return queue.popleft()


if __name__ == '__main__':
    test_name_list = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
    print(hot_potato(test_name_list, 7))
