# DECLARE full_name, snake_case_name

# INPUT full_name
full_name = input("please enter your full name in incorrect casing: ")

# INPUT snake_case_name
snake_case_name = full_name.lower().replace(" ", "_")

# PRINT
print(snake_case_name)