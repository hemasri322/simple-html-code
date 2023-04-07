import time
import random
import matplotlib.pyplot as plt

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[l] > arr[largest]:
            largest = l
        if r < n and arr[r] > arr[largest]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

# Test the sorting algorithms and measure their execution time
ns = [1000, 2000, 3000, 4000, 5000]
insertion_sort_times = []
heap_sort_times = []

for n in ns:
    arr = [random.randint(1, 1000) for _ in range(n)]
    start_time = time.time()
    insertion_sort(arr)
    end_time = time.time()
    insertion_sort_times.append(end_time - start_time)

    arr = [random.randint(1, 1000) for _ in range(n)]
    start_time = time.time()
    heap_sort(arr)
    end_time = time.time()
    heap_sort_times.append(end_time - start_time)

# Plot the results
plt.plot(ns, insertion_sort_times, label='Insertion Sort')
plt.plot(ns, heap_sort_times, label='Heap Sort')
plt.xlabel('Number of elements (n)')
plt.ylabel('Execution time (seconds)')
plt.legend()
plt.show()
