'''
Fahrenheit to Celsius:

Write the necessary code to read a degree in Fahrenheit from the console
then convert it to Celsius and print it to the console.

    C = (F - 32) * (5 / 9)

Output should read like - "81.32 degrees fahrenheit = 27.4 degrees celsius"


'''

temperature = int(input("Enter a temperature in Fahrenheit to have it converted to Celsius: "))
conversion = (temperature - 32) * (5/9)
print(temperature, "degrees fahrenheit =", conversion, "degrees celsius.")
