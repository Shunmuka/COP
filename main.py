#Shunmuka
def encode(password):
    encoded_password = ""

    for digit in password:
        # Shift each digit up by 3 numbers
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit

    return encoded_password

def decoder(password):
    str_number = str(password)
    new_number = ""
    for i in str_number:
        new_number += str(int(i)-3)
    return new_number

def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        choice = input("Please enter an option: ")

        if choice == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print(f"Your password has been encoded and stored!")
        elif choice == "2":
            print(f'The encoded password is {encoded_password}, and the original password is {password}.')
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please enter a valid option (1, 2, or 3).")


if __name__ == "__main__":
    main()
