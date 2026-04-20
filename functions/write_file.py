import os

def write_file(working_directory, file_path, content):

    working_path = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_path, file_path))

    check_path_prefix = os.path.commonpath([working_path, target_file]) == working_path
    if not check_path_prefix:
        return(f"Error: Cannot write to \"{file_path}\" as it is outside the permitted working directory")

    check_path_sufix = os.path.isdir(target_file)
    if check_path_sufix:
        return(f"Error: Cannot write to \"{file_path}\" as it is a directory")

    os.makedirs(os.path.dirname(target_file), exist_ok=True)

    try:
        with open(target_file, mode='w') as f:
           f.write(content)

        return(f"Successfully wrote to \"{file_path}\" ({len(content)} characters written)")

    except:
        return(f"Error: cannot open or write {target_file}")
