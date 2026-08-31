# Ask the user to for width and continue looping until they
# Enter a number more or not equal to 0
def int_check(question, low):
    error = f"Please enter a number that is more or equal to {low}\n make sure to not add decimals!"
    while True:

        try:
            # ask the human for a number
            response = int(input(question))

            # check that the number is more than 0
            if response >= low:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

# Main Routine goes here
for item in range(0, 2):
    integer = int_check("Integer: ",0)
    print(integer)

print()

for item in range(0, 2):
    width = int_check("Width: ",1)
    print(width)

print()

for item in range(0, 2):
    height = int_check("Height: ", 1)
    print(height)
