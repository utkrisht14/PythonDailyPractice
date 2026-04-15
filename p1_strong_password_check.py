def check_password(password):
    errors = []

    if len(password) < 8:
        errors.append("Password is too short")
    if not any(char.isupper() for char in password):
        errors.append("Must contain at least one uppercase letter")
    if not any(char.islower() for char in password):
        errors.append("Must contain at least one lowercase letter")
    if not any(char.isdigit() for char in password):
        errors.append("Must contain at least one digit")

    if errors:
        for error in errors:
            print(error)
        return False
    else:
        print("Password is acceptable!")
        return True

