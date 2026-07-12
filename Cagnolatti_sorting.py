import time
import numpy
import random

# Define sorting algorithms and list sizes
sorting_algorithms = ['Bubble Sort', 'Selection Sort', 'Insertion Sort', 'Merge Sort', 'Quick Sort', 'Python Sort', 'NumPy Sort']
list_sizes = [100, 1000, 10000, 100000, 500000]

# -----------------------------------
# ------ FUNCTION DEFINITIONS -------
# -----------------------------------

# Bubble Sort algorithm
def bubble_sort(sequence):
    length = len(sequence)
    for i in range(length - 1):
        for j in range(length - i - 1):
            if sequence[j] > sequence[j + 1]:
                sequence[j], sequence[j + 1] = sequence[j + 1], sequence[j]
    return sequence

# Selection Sort algorithm
def selection_sort(sequence):
    length = len(sequence)
    for i in range(length):
        min_idx = i
        for j in range(i + 1, length):
            if sequence[j] < sequence[min_idx]:
                min_idx = j
        sequence[min_idx], sequence[i] = sequence[i], sequence[min_idx]
    return sequence

# Insertion Sort algorithm
def insertion_sort(sequence):
    length = len(sequence)
    for i in range(1, length):
        j = i
        while j > 0 and sequence[j - 1] > sequence[j]:
            sequence[j], sequence[j - 1] = sequence[j - 1], sequence[j]
            j -= 1
    return sequence

# Merge Sort algorithm
def merge_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    mid = length // 2
    left_half = sequence[:mid]
    right_half = sequence[mid:]
    merge_sort(left_half)
    merge_sort(right_half)
    i = j = k = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            sequence[k] = left_half[i]
            i += 1
        else:
            sequence[k] = right_half[j]
            j += 1
        k += 1
    while i < len(left_half):
        sequence[k] = left_half[i]
        i += 1
        k += 1
    while j < len(right_half):
        sequence[k] = right_half[j]
        j += 1
        k += 1
    return sequence

# Quick Sort algorithm
def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()
    items_greater = []
    items_lower = []
    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

# Function to check if the list was sorted correctly
def is_sorted(sequence):
    return sequence == sorted(sequence)

# -----------------------------------
# ------------ MAIN LOOP ------------
# -----------------------------------

# Loop through each algorithm for each list size
for size in list_sizes:
    print(f"\n{size} random integers sorted in:")
    for algorithm in sorting_algorithms:

        # Generate a new random integer list, reset the solution, and start the stopwatch
        random_list = [random.randint(1, size) for x in range(size)]
        sorted_list = []
        start_time = time.time()

        # Bubble Sort
        if algorithm == 'Bubble Sort':
            sorted_list = bubble_sort(random_list)

        # Selection Sort
        elif algorithm == 'Selection Sort':
            sorted_list = selection_sort(random_list)

        # Insertion Sort
        elif algorithm == 'Insertion Sort':
            sorted_list = insertion_sort(random_list)

        # Merge Sort
        elif algorithm == 'Merge Sort':
            sorted_list = merge_sort(random_list)

        # Quick Sort
        elif algorithm == 'Quick Sort':
            sorted_list = quick_sort(random_list)

        # Python Sort
        elif algorithm == 'Python Sort':
            sorted_list = random_list
            list.sort(sorted_list)

        # NumPy Sort
        elif algorithm == 'NumPy Sort':
            sorted_list[:] = numpy.sort(random_list)[:]

        # Stop the stopwatch and record the execution time
        end_time = time.time()
        execution_time = end_time - start_time

        # Check if the list was correctly sorted and display execution time
        if is_sorted(sorted_list):
            print(f"\t{execution_time: .6f} seconds by {algorithm}")