# This is a program to determine if someone is able to buy alcohol.



# Function to check if the age is 21 or older
def is_of_legal_age(age):
    # Checks if the age is 21 or more
    if age >= 21:
        return True
    else:
        return False


if __name__ == "__main__":
    # Input: Ask the user for their age
    age = int(input("Enter Your Age: "))

    # Call the is_of_legal_age function and store the result
    legal_age = is_of_legal_age(age)

    # Output: Prints if the person is of legal age or not
    if legal_age:
        print("You may be able to buy alcohol.")
    else:
        print("You are not of legal age. You will now be redirected out of the website. Good bye.")