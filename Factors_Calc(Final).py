# Ask the user whether they want to start with or without instructions
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")

# Ask if the user wants to use code with or without instruction. Show if they want to and no if they said 'no'
def instructions():
    statement_generator("Instructions","-")

    print('''
To use the progress, you simply need to type in a number that is equal or more than 1 to less or equal 200
the program will also show the numbers' factor based on your chosen integer

The program will also say if your chosen number is a prime number, or a perfect square :)
- Is a prime number
- Or if it's a perfect square
''')
want_instructions = input("Press <Enter> to see instruction or type anything then press <Enter> to Run with no Instructions ")
if want_instructions == "":
    instructions()
print()
print(" Alrighty, let's proceed")
print()

# keep asking the user on what their Integer is while making sure it's between 1-200. it does not be less or more than that
# All while asking question again if the user put something less than 1 or more than 200
def num_check(question):

    error = f"Please enter a number that is between 1 and 200 inclusive\n"
    while True:

        response = input(question).lower()
        if response == "xxx":
            return response

        try:
            # Ask the user for a number
            response = int(response)

            # Check that the number is higher than zero
            if 1 <= response <= 200:
                return response
            else:
                print(error)
        except ValueError:
            print(error)
# Shut the code down if they said 'xxx'
while True:
    to_factor = num_check("Numbers to factor? Or 'xxx' to quit: ")
    print("You chose to factor", to_factor)
# If the user says 'xxx' instead, then end the program
    if to_factor == "xxx":
        break

