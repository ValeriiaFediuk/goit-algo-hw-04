import timeit
import random

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def test_sorting_algorithm(sort_func, data):
    arr = data.copy()
    start_time = timeit.default_timer()
    sort_func(arr)
    end_time = timeit.default_timer()
    return end_time - start_time

data_sizes = [10**3, 10**4, 10**5]
test_data = {size: [random.randint(0, size) for _ in range(size)] for size in data_sizes}

for size, data in test_data.items():
    print(f"Розмір набору даних: {size}")
    time_merge = test_sorting_algorithm(merge_sort, data)
    time_insertion = test_sorting_algorithm(insertion_sort, data)
    time_timsort = timeit.timeit(lambda: sorted(data), number=1)
    print(f"Час сортування злиттям: {time_merge}")
    print(f"Час сортування вставками: {time_insertion}")
    print(f"Час сортування Timsort: {time_timsort}")
    print()
