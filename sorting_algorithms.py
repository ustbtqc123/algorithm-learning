def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


def bubble_sort(array):
    swapped = False
    n = len(array)
    for i in range(n - 1):
        for j in range(1, n - i):
            if array[j] < array[j - 1]:
                swap(array, j, j - 1)
                swapped = True
        if not swapped:
            break


def selection_sort(array):
    n = len(array)
    for i in range(n - 1):
        k = i
        for j in range(i + 1, n):
            if array[j] < array[k]:
                k = j
        if k != i:
            swap(array, i, k)


def insert_sort(array):
    n = len(array)
    for i in range(1, n):
        base = array[i]
        j = i - 1
        while j >= 0 and array[j] > base:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = base


def quick_sort(array, left, right):
    if left >= right:
        return
    i, j = left, right
    pivot = array[left]
    while i < j:
        while i < j and array[j] >= pivot:
            j -= 1
        while i < j and array[i] <= pivot:
            i += 1
        swap(array, i, j)
    swap(array, i, left)
    quick_sort(array, left, i - 1)
    quick_sort(array, i + 1, right)


if __name__ == '__main__':
    test_list = [100, 5, 4, 6, 190, 15, 13, 648]
    # result = sorted(test_list)
    # bubble_sort(test_list)
    # selection_sort(test_list)
    # insert_sort(test_list)
    quick_sort(test_list, 0, len(test_list) - 1)
    print(test_list)
