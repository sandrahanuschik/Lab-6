def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = int(input("Please enter an option: "))
        # password = int(password)
        if option == 1:
            password = input("Please enter your password to encode: ")
            if len(password) >= 8:
                encode = ""
                for element in password:
                    if element.isdigit():
                        element = int(element)
                        element += 3
                        encode += str(element)
                print("Your password has been encoded and stored!\n")
        if option == 2:
            encode = str(encode)
            decode = ""
            for element in encode:
                element = int(element) - 3
                decode += str(element)
            print(f"The encoded password is {encode}, and the original password is {decode}.\n")




if __name__ == "__main__":
    main()
