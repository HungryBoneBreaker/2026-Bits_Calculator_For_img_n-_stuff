# Ask user if they want (Image, Text, Integer)

def get_filetype():

    while True:
        response = input("File type: ").lower()
        # check i or the exit code
        if response == "xxx" or response == "i":
            return response

        # check if user ask for integer
        elif response in ['integer', 'int']:
            return "integer"

        # check if response is image
        elif response in ['picture', 'image', 'img', 'p']:
            return "image"

        # check for text
        elif response in ['text', 'txt', 't']:
            return "text"

        # if the response is INVALID
        else:
            print("Please enter only files types shown in instruction")

# Main routine goes here
while True:
    file_type = get_filetype()

# Ask user if they want image or integer whenever they type 'i'
    if file_type == 'i':

        want_image = input("Press <Enter> for an integer or any key for an image")
        if want_image == "":
            file_type = "integer"
        else:
            file_type = "image"


    print(f"You've chose the {file_type} file type")

    if file_type == "xxx" :
        break
