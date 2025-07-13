from google.genai import types

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
            "debug": types.Schema(
                type=types.Type.STRING,
                description='''Toggle debug mode. This is defaulted to "False"''',
            ),
        },
    ),
)

schema_create_folder = types.FunctionDeclaration(
    name="create_folder",
    description="Create a folder in the specified directory, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "folder_path": types.Schema(
                type=types.Type.STRING,
                description='''The whole path of the folder you want to create.''',
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
        schema_create_folder,
    ]
)