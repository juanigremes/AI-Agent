import os
from config import MAX_CHARS_TO_READ


def get_file_content(working_directory, file_path):

    working_path = os.path.abspath(working_directory)
    path_to_file = os.path.normpath(os.path.join(working_path, file_path)) 
    
    check_path_prefix = os.path.commonpath([working_path, path_to_file]) == working_path
    if not check_path_prefix:
        return(f"Error: Cannot read \"{file_path}\" as it is outside the permitted working directory")

    check_path_sufix = os.path.isfile(path_to_file)
    if not check_path_sufix:
        return(f"Error: File not found or is not a regular file: \"{file_path}\"")

    try:
        # open file
        with open(path_to_file) as file:
            content = file.read(MAX_CHARS_TO_READ)
            if file.read(1):
                content += f"[...File \"{file_path}\" truncated at {MAX_CHARS_TO_READ} characters]"
    except:
        return(f"Error: cannot open or read {path_to_file}")

    return(content)
