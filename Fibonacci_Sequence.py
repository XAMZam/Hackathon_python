def generate_fibonacci_sequence(n):
    fibonacci_sequence = [0, 1]
    for i in range(2, n):
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)
    return fibonacci_sequence

def main():
    # Ask the user to input the value of n
    n = int(input("Enter the number of terms for the Fibonacci sequence: "))
    
    # Generate the Fibonacci sequence
    fibonacci_sequence = generate_fibonacci_sequence(n)
    
    # Print the generated Fibonacci sequence
    print("Generated Fibonacci sequence:")
    print(fibonacci_sequence)

if __name__ == "__main__":
    main()
