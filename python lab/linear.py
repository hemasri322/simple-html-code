import random
import time
import matplotlib.pyplot as plt

def linear_search(arr, x):
    """
    Performs a linear search to find the index of x in arr.
    Returns -1 if x is not found in arr.
    """
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# Generate lists of different sizes and time how long it takes to perform a linear search on them
sizes = [10, 100, 1000, 10000, 100000]
times = []

for size in sizes:
    arr = [random.randint(0, 100000) for _ in range(size)]
    x = arr[-1]
    start_time = time.time()
    linear_search(arr, x)
    end_time = time.time()
    times.append(end_time - start_time)

# Plot the results
plt.plot(sizes, times)
plt.xlabel('Size of List')
plt.ylabel('Time (Seconds)')
plt.show()