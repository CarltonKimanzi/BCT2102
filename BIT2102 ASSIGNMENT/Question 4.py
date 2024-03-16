def celsius_to_fahrenheit(celsius):

  return (celsius * 9/5) + 32

try:
  celsius = float(input("Enter a temperature in Celsius: "))
except ValueError:
  print("Invalid input. Please enter a number.")
  exit()

fahrenheit = celsius_to_fahrenheit(celsius)

print(f"{celsius:.2f} degrees Celsius is equal to {fahrenheit:.2f} degrees Fahrenheit.")
