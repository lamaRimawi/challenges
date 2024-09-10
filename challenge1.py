def generate_fibonacci(n):
    if not isinstance(n, int) or n < 0:
        print("Invalid input: Please enter a non-negative integer.")
        return

    fib_sequence = [0, 1]

    if n == 0:
        return [0]
    elif n == 1:
        return fib_sequence[:2]

    while len(fib_sequence) < n + 1:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)

    return fib_sequence



n = input("Enter the number of Fibonacci terms you want: ")
try:
    n = int(n)
    fib_sequence = generate_fibonacci(n)
    print(f"Fibonacci sequence up to {n} terms: {fib_sequence}")
except ValueError:
    print("Invalid input: Please enter a valid integer.")
