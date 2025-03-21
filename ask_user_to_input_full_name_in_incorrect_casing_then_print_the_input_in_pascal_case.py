# DECLARE full_name, pascal_case_name

# INPUT full_name
full_name = input("Please enter your full name in incorrect casing: ")

# INPUT pascal_case_name
pascal_case_name = full_name.title().replace(" ", "")
# PRINT
print(pascal_case_name)