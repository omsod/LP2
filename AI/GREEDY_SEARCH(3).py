def greedy_selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"Step {i+1}: {arr}")

# Take input from user
size = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter the elements separated by space: ").split()))

# Optional: Check if user entered correct number of elements
if len(arr) != size:
    print("Error: Number of elements does not match the given size.")
else:
    print("Original array:", arr)
    greedy_selection_sort(arr)
    print("Sorted array:  ", arr)
