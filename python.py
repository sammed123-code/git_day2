def lomuto_partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Example usage
if __name__ == "__main__":
    arr = [10, 80, 30, 90, 40, 50, 70]
    low = 0
    high = len(arr) - 1
    pivot_index = lomuto_partition(arr, low, high)
    print(f"Partitioned array: {arr}")
    print(f"Pivot index: {pivot_index}")