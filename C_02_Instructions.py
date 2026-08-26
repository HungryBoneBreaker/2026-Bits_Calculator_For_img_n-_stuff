# Generates headings (eg:---- Heading ----)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Display function here
def instructions():
    statement_generator("Instruction","-")

    print('''
Instructions goes here
- Instruction 1
- Instruction 2
- whatever anything left
''')

#Main Routine goes here

# Display instruction if client commanded so
want_instructions = input("Press <Enter> to see instruction or type anything then press <Enter> to Run with no Instructions")


if want_instructions == "":
    instructions()

print("Continue program we go")