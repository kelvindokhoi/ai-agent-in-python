import os
from google.genai import types

def get_files_info(working_directory, directory):
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

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description='''The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself. "root" or "no specific directory" should map to '.'.''',
            ),
        },
    ),
)

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Retrieve a file's content in the specified directory, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description='''The path to the file you want to retrieve the content.''',
            ),
        },
    ),
)

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Run python file in the specified directory, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description='''The file path of the python file you want to run.''',
            ),
        },
    ),
)

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write to a file in the specified directory, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description='''The file path of the file you want to overwrite.''',
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description='''The new content of the file''',
            ),
        },
    ),
)

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)