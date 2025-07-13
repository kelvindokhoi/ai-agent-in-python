import os
from google.genai import types

def get_files_info(working_directory, directory="."):
    try:
        original_dir = directory
        directory = os.path.abspath(os.path.join(working_directory,directory))
        if not directory.startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot list "{original_dir}" as it is outside the permitted working directory'
        if not os.path.isdir(directory):
            return f'Error: "{original_dir}" is not a directory'
        all_items_formatted = []
        for item in os.listdir(directory):
            name = item
            item = os.path.join(directory,item)
            all_items_formatted.append(f"- {name}: file_size={os.path.getsize(item)} bytes, is_dir={os.path.isdir(item)}")
        return "\n".join(all_items_formatted)
    except Exception as e:
        return f'Error:{e}'

