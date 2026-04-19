
errors = []

def password_checker(password):
    if any(text.isspace() for text in password):
        print("Password cannot contain spaces.")
        return False
    special_characters = ["!","@","#","$","%","^","&","*"]
    # Check for at least 8 character long
    if len(password) < 8:
        errors.append("Password is too short")
    # Contain at least one upper case
    if not any(text.isupper() for text in password):
        errors.append("Must contain at least one uppercase letter")
    # Contain at least one lower case
    if not any(text.islower() for text in password):
        errors.append("Must contain at least one lowercase letter")
    # Contain at least one digit
    if not any(text.isnumeric() for text in password):
        errors.append("Must contain at least one digit")
    # Contain at least one special character
    if not any(char in special_characters for char in password):
        errors.append("Must contain at least one special character")

    for error in errors:
        if len(errors) > 0 & len(errors) < 3:
            print(error)
        elif len(errors) == 0:
            print("Strong password.")
        elif len(errors) >= 3:
            print("Moderate password.")
        else:
            print("Weak password.")


# Provide the score based on the error of password
def score_provider():
    score_value = 5 - len(errors)
    print(f"score: {score_value}/5")

# Check for the errors
password_checker(input("Enter your password: "))
score_provider()