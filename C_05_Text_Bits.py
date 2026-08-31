
def calc_text_bits():
    pass
# Get text from client
    response = input("Please Enter some text you want it's bits to be calculated: ")

#Calculate the amount of bits needed
    num_chars = len(response)
    num_bits = num_chars * 8

# Set up answer and respond to client
    answer = (f"{response} has {num_chars} characters."
          f"\n We need {num_chars} x 8 bits to represent it"
          f"\n which is {num_bits} bits")

    return answer

# Routine goes here :)
text_ans = calc_text_bits()
print(text_ans)