import os
from functions.config import *


def get_file_content(working_directory, file_path):
    try:
        original_dir = file_path
        file_path = os.path.abspath(os.path.join(working_directory,file_path))
        if not file_path.startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot read "{original_dir}" as it is outside the permitted working directory'
        if not os.path.isfile(file_path):
            return f'Error: File not found or is not a regular file: "{original_dir}"'
        
        with open(file_path,'r') as f:
            text = f.read()
            if len(text)>CHARACTER_LIMIT:
                text = f'{text[:CHARACTER_LIMIT-1]}\n[...File "{original_dir}" truncated at 10000 characters]'
            return text
    except Exception as e:
        return f"Error:{e}"