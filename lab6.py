def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = int(input("Please enter an option: "))
        password = input("Please enter your password to encode: ")
        # password = int(password)
        if len(password) >= 8:
            if option == 1:
                encode = ""
                for element in password:
                    if element.isdigit():
                        element = int(element)
                        element += 3
                        encode += str(element)
                print(encode)

if __name__ == "__main__":
    main()