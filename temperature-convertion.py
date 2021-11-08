def fahrenheit_to_celsius():
    Fahrenheit = int(input("Enter a temperature in Fahrenheit: "))
    Celsius = (Fahrenheit - 32) * 5.0/9.0
    print("Temperature:", Fahrenheit, "Fahrenheit = ", Celsius, " C")

def celsius_to_fahrenheit():
    Celsius = int(input("Enter a temperature in Celsius: "))
    Fahrenheit = 9.0/5.0 * Celsius + 32
    print("Temperature:", Celsius, "Celsius = ", Fahrenheit, " F")

if __name__=="__main__":
    print("Options:")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    option = int(input("Select an option [1/2]:"))
    if(option == 1):
        fahrenheit_to_celsius()
    else:
        celsius_to_fahrenheit()