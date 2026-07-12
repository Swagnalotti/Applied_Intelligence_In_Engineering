# import time
# import random
#
# def bubble_sort(myList):
#     n = len(myList)
#     for i in range(n - 1):
#         for j in range(n - i - 1):
#             if myList[j] > myList[j + 1]:
#                 myList[j], myList[j + 1] = myList[j + 1], myList[j]
#
# def selection_sort(myList):
#     n = len(myList)
#     for i in range(n):
#         min_index = i
#         for j in range(i + 1, n):
#             if myList[j] < myList[min_index]:
#                 min_index = j
#         myList[min_index], myList[i] = myList[i], myList[min_index]
#
# def mergeSort(arr):
#     if len(arr) <= 1:
#         return arr
#
#     mid = len(arr) // 2
#     leftHalf = arr[:mid]
#     rightHalf = arr[mid:]
#
#     sortedLeft = mergeSort(leftHalf)
#     sortedRight = mergeSort(rightHalf)
#
#     return merge(sortedLeft, sortedRight)
#
# def merge(left, right):
#     result = []
#     i = j = 0
#
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#
#         result.extend(left[i:])
#         result.extend(right[j:])
#
#         return result
#
# #Bubble sort
# a = [random.randint(1, 10) for x in range(1000)]
# start_time = time.time()
# bubble_sort(a)
# print(f"Bubble sort time: {time.time() - start_time : .4f} seconds")
#
# #Selection sort
# b = [random.randint(1, 10) for x in range(1000)]
# start_time = time.time()
# selection_sort(b)
# print(f"Selection sort time: {time.time() - start_time : .4f} seconds")
#
# #Merge sort
# c = [random.randint(1, 10) for x in range(1000)]
# start_time = time.time()
# mergeSort(c)
# print(f"Merge sort time: {time.time() - start_time : .4f} seconds")
#
# #Python sort
# d = [random.randint(1, 10) for x in range(1000)]
# start_time = time.time()
# d.sort()
# print(f"Power sort time: {time.time() - start_time : .4f} seconds")