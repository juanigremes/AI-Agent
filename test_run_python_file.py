from functions.run_python_file import run_python_file


test1 = run_python_file("calculator", "main.py")
print(f"Result for current directory:{test1}")

test2 = run_python_file("calculator", "main.py", ["3 + 5"])
print(f"Result for 'pkg' directory:{test2}")

test3 = run_python_file("calculator", "tests.py")
print(f"Result for '/bin' directory:{test3}")

test4 = run_python_file("calculator", "../main.py")
print(f"Result for '../' directory:{test4}")

test5 = run_python_file("calculator", "nonexistent.py")
print(f"Result for '../' directory:{test5}")

test6 = run_python_file("calculator", "lorem.txt")
print(f"Result for '../' directory:{test6}")

