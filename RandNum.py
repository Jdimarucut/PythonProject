import random

def function(x):
    return 2 * x + 1


random_numbers = [random.randint(-10, 10) for _ in range(10)]


input_x = [function(num) for num in random_numbers]


sorted_numbers = sorted(random_numbers)
sorted_results = sorted(input_x)


print("Original list:", random_numbers)
print("Result list (2x + 1):", input_x)
print("Sorted list:", sorted_numbers)
print("Output", sorted_results)