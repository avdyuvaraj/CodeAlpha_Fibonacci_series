nterms = input("Enter the number of Fibonacci terms to generate: ")

try:
    n = int(nterms)
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        
        a, b = 0, 1
        count = 0
        print(f"Fibonacci sequence for the first {n} terms:")
        while count < n:
            print(a, end=' ')
            a, b = b, a + b
            count += 1
        print()
except ValueError:
    print("Invalid input. please enter a positive integer.")