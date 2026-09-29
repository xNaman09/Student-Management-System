def validate_name(name):
    return bool(name.strip()) and name.replace(" ", "").isalpha()

def validate_age(age):
    try:
        age = int(age)
        return 1 <= age <= 100
    except:
        return False

def validate_marks(marks):
    try:
        marks = float(marks)
        return 0 <= marks <= 100
    except:
        return False

def validate_email(email):
    return "@" in email and "." in email
