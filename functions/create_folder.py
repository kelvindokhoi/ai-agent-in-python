import os

def create_folder(folder_path, working_directory='.'):
    try:
        combined_path = os.path.abspath(os.path.join(working_directory, folder_path))
        if not combined_path.startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot create folder "{folder_path}" as it is outside the permitted working directory'
        
        os.makedirs(combined_path, exist_ok=True)
        return f'Successfully created folder "{folder_path}"'
        
    except Exception as e:
        return f"Error: {e}"