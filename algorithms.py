import time

def bubble_sort(arr, draw_callback, delay):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                draw_callback(arr, ['green' if x == j or x == j+1 else 'red' for x in range(len(arr))])
                time.sleep(delay)
    draw_callback(arr, ['green' for _ in range(len(arr))])
