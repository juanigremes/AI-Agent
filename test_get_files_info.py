from functions.get_files_info import get_files_info


test1 = get_files_info("calculator", ".")
print(f"Result for current directory:{test1}")

test2 = get_files_info("calculator", "pkg")
print(f"Result for 'pkg' directory:{test2}")

test3 = get_files_info("calculator", "/bin")
print(f"Result for '/bin' directory:{test3}")

test4 = get_files_info("calculator", "../")
print(f"Result for '../' directory:{test4}")

