def linear_search(my_list, target):
    n = len(my_list)

    for i in range(n):
        if my_list[i] == target:
            return i

    return -1

def binary_search(my_list, target):

    low = 0
    high = len(my_list) - 1
    while low <= high:
        mid = low + (high - low) // 2

        if my_list[mid] == target:
            return mid

        if my_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6
print(linear_search(my_list, target))
print(binary_search(my_list, target))