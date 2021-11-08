def fibonacci_sequence(n):
    sequence = []
    for x in range(n):
        if x == 0 or x == 1:
            sequence.append(1)
        else:
            sequence.append(sequence[-1] + sequence[-2])
    print(", ".join(map(str, sequence)))

if __name__ == "__main__":
    n = int(input("enter a number: "))
    fibonacci_sequence(n)