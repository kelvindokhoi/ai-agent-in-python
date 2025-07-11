import os

def write_file(working_directory, file_path, content):
    try:
        combined_path = os.path.abspath(os.path.join(working_directory,file_path))
        if not combined_path.startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        with open(combined_path,'w') as f:
            if f.write(content):
                return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Errors:{e}"
    
    