import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    working_path = os.path.abspath(working_directory)
    path_to_file = os.path.normpath(os.path.join(working_path, file_path)) 
    
    check_path_prefix = os.path.commonpath([working_path, path_to_file]) == working_path
    if not check_path_prefix:
        return(f"Error: Cannot execute \"{file_path}\" as it is outside the permitted working directory")

    check_path_sufix = os.path.isfile(path_to_file)
    if not check_path_sufix:
        return(f"Error: \"{file_path}\" does not exist or is not a regular file")

    check_file_format = file_path.endswith(".py")
    if not check_file_format:
        return(f"Error: \"{file_path}\" is not a Python file")
    
    try:
        command = ["python", path_to_file]
        if args != None:
            command.extend(args)

        completed_process = subprocess.run(command, capture_output=True, timeout=30, text=True)
    
        res = ''
        if completed_process.returncode != 0:
            res += f"Process exited with code {completed_process.returncode}\n"
    
        if completed_process.stdout != "":
            res += f"STDOUT: {completed_process.stdout}\n"
        elif completed_process.stderr == "":
            res += "No output produced\n"
        else:
            res += f"STDERR: {completed_process.stderr}"
   
        return(res)
    except Exception as e:
        return(f"Error: executing Python file: {e}")
