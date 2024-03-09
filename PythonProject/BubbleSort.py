def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Get user input for a list of numbers
numbers = []
for i in range(10):
    number = int(input(f"Enter number {i+1}: "))
    numbers.append(number)

# Print the unsorted list
print("Unsorted list:", numbers)

# Sort the list using Bubble Sort
bubble_sort(numbers)

# Print the sorted list
print("Sorted list:", numbers)

# Get user input for the number to search
search_number = int(input("Enter the number to search: "))

# Perform linear search and print the result
result = linear_search(numbers, search_number)
if result != -1:
    print(f"{search_number} found at index {result} after sorting.")
else:
    print(f"{search_number} not found in the list.")