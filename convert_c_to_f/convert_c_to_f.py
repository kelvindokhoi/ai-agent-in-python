def celsius_to_fahrenheit(celsius):
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit

if __name__ == "__main__":
  celsius_value = float(input("Enter temperature in Celsius: "))
  fahrenheit_value = celsius_to_fahrenheit(celsius_value)
  print(f"{celsius_value} degrees Celsius is equal to {fahrenheit_value} degrees Fahrenheit")