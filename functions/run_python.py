import os
import subprocess

def run_python_file(working_directory, file_path):
    combined_path = os.path.abspath(os.path.join(working_directory,file_path))
    if not combined_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(combined_path):
        return f'Error: File "{file_path}" not found.'
    if not combined_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        result = subprocess.run(['python',combined_path],timeout=30,capture_output=True,cwd=working_directory)
        output = result.stdout.decode()
        errput = result.stderr.decode()
        if output.strip() == '' and errput.strip() == '':
            return  "No output produced."
        message = f"STDOUT:{output}\nSTDERR:{errput}"
        if result.returncode != 0:
            message += f"\nProcess exited with code {result.returncode}"
        return message
    except Exception as e:
        return f"Error: executing Python file: {e}"