def fahrenheit_to_celsius(fahrenheit):
  celsius = (fahrenheit - 32) * 5/9
  return celsius

if __name__ == "__main__":
  fahrenheit = float(input("Enter temperature in Fahrenheit: "))
  celsius = fahrenheit_to_celsius(fahrenheit)
  print(f"{fahrenheit} Fahrenheit is equal to {celsius} Celsius")