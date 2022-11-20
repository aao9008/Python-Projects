def main():
    print('Please enter a temperature in Fahrenheit:')
    fahr = float(input())
    cel = fahrenheit_to_celsius(fahr)
    # cel is storing variable returned variable C
    print(fahr,'Fahrenheit is',cel,'Celsius')

def fahrenheit_to_celsius(F):
    C = (F-32) * (5/9)
    return C
main()