import subprocess

fahrenheit = 68

result = subprocess.run(["python", "convert_f_to_c.py", str(fahrenheit)], capture_output=True, text=True)

print(result.stdout)