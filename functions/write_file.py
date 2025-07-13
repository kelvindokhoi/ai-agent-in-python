import os

def write_file(file_path, content, working_directory='.',debug=False):
    if debug:
        print(f"DEBUG: Attempting to write to {file_path}")
        print(f"DEBUG: Working directory: {working_directory}")
    
    try:
        combined_path = os.path.abspath(os.path.join(working_directory, file_path))
        if debug:print(f"DEBUG: Combined path: {combined_path}")
        
        if not combined_path.startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        if debug:print(f"DEBUG: About to write {len(content)} characters")
        with open(combined_path, 'w') as f:
            chars_written = f.write(content)
            if debug:print(f"DEBUG: Wrote {chars_written} characters")
        
        if debug:
            if os.path.exists(combined_path):
                print(f"DEBUG: File exists after writing")
            else:
                print(f"DEBUG: File does NOT exist after writing!")
            
        return f'Successfully wrote to "{file_path}" ({chars_written} characters written)'
        
    except Exception as e:
        if debug:print(f"DEBUG: Exception occurred: {e}")
        return f"Error: {e}"