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


# Calculate how many bits is needed for Images
def image_calc():
    width = int_check("Width: ",1)
    height = int_check("Height: ", 1)


# Calculate the amount of pixel and multiply by 24 to get the number of bits
    num_pixels = width * height
    num_bits = num_pixels * 24

# Answer and return it to user
    answer = (f"Number of pixels: {width} x {height} = {num_pixels} "
              f"\nNumber of bits: {num_pixels} x 24 = {num_bits}")

    return answer


# Main routine goes here
image_ans = image_calc()
print(image_ans)
