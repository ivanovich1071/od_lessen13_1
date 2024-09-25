import time
import random

# Пузырьковая сортировка (Bubble Sort)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Сортировка выбором (Selection Sort)
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Сортировка вставками (Insertion Sort)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Быстрая сортировка (Quick Sort)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Сортировка слиянием (Merge Sort)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Тестирование алгоритмов
def test_sorting_algorithm(sort_func, arr):
    print(f"Тестирование {sort_func.__name__}:")
    print("Исходный массив:", arr)
    start_time = time.time()
    if sort_func in [quick_sort, merge_sort]:
        sorted_arr = sort_func(arr.copy())  # Quick Sort и Merge Sort возвращают новый массив
    else:
        sorted_arr = arr.copy()
        sort_func(sorted_arr)
    print("Отсортированный массив:", sorted_arr)
    print(f"Время выполнения: {time.time() - start_time:.6f} секунд\n")

# Оценка временной сложности
def evaluate_complexity(sort_func, size=1000):
    print(f"Оценка сложности для {sort_func.__name__}:")
    arr = [random.randint(0, 10000) for _ in range(size)]
    start_time = time.time()
    if sort_func in [quick_sort, merge_sort]:
        sort_func(arr.copy())
    else:
        sort_func(arr.copy())
    print(f"Время выполнения для {size} элементов: {time.time() - start_time:.6f} секунд\n")

# Основная функция для запуска тестов
def main():
    # Пример массива
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorting_algorithms = [bubble_sort, selection_sort, insertion_sort, quick_sort, merge_sort]

    for sort_func in sorting_algorithms:
        test_sorting_algorithm(sort_func, arr)
        evaluate_complexity(sort_func)

if __name__ == "__main__":
    main()
