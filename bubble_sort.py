def bubble_sort(array: list) -> list:
    n = len(array)
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                # Swap if elements are in the wrong order
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

# Example usage
arr = [64, 25, 12, 22, 11]
sorted_arr = bubble_sort(arr)
print(sorted_arr)  # Output: [11, 12, 22, 25, 64]
