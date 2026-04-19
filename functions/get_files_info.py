import os


def get_files_info(working_directory, directory="."):
    working_path = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_path, directory))

    check_path_prefix = os.path.commonpath([working_path, target_dir]) == working_path
    if not check_path_prefix:
        return(f"Error: Cannot list \"{directory}\" as it is outside the permitted working directory")

    check_path_sufix = os.path.isdir(target_dir)
    if not check_path_sufix:
        return(f"Error: \"{directory}\" is not a directory")

    res = '\n'
    for element in os.listdir(target_dir):
        try:
            path = os.path.join(target_dir, element)
            is_dir = os.path.isdir(path)
            file_size = os.path.getsize(path)
        except: 
            return("Error: isdir or getsize function gone wrong")
        res = res + f" - {element}: file_size={file_size} bytes, is_dir={is_dir} \n"

    return res
