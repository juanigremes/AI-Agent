from functions.write_file import write_file 

test0 = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
print(f"Result for current directory:{test0}")

test1 = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
print(f"Result for current directory:{test1}")

test2 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
print(f"Result for 'pkg' directory:{test2}")


