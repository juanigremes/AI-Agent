from functions.get_file_content import get_file_content

test0 = get_file_content("calculator", "lorem.txt")
print(f"Result for current directory:{test0}")

test1 = get_file_content("calculator", "main.py")
print(f"Result for current directory:{test1}")

test2 = get_file_content("calculator", "pkg/calculator.py")
print(f"Result for 'pkg' directory:{test2}")

test3 = get_file_content("calculator", "/bin/cat")
print(f"Result for '/bin' directory:{test3}")

test4 = get_file_content("calculator", "pkg/does_not_exist.py")
print(f"Result for '../' directory:{test4}")

