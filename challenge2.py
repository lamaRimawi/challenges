def find_missing_numbers(arr):
    if not all(isinstance(x, int) for x in arr):
        print("Invalid input: All elements must be integers.")
        return

    if not arr:
        print("Invalid input: The array cannot be empty.")
        return

    arr = sorted(arr)
    full_range = set(range(arr[0], arr[-1] + 1))
    missing_numbers = full_range - set(arr)

    return sorted(list(missing_numbers))



input_series = input("Enter a series of numbers separated by commas: ")
try:
    input_list = [int(x.strip()) for x in input_series.split(",")]
    missing_numbers = find_missing_numbers(input_list)
    if missing_numbers:
        print(f"Missing numbers: {missing_numbers}")
    else:
        print("No missing numbers. The series is a perfect range.")
except ValueError:
    print("Invalid input: Please enter a valid series of integers separated by commas.")
