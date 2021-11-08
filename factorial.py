def factorial(n):
    result = 1
    for x in range(n):
        result *= n-x
    return result
    
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print("factorial of " , n , " is " , factorial(n))