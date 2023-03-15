def is_email_valid(func):
    def wrapper(email, y, a, z, b, c):
        if "@" in email:
            if "." in email.split("@")[1]:
                func(email, y, a, z, b, c)
            else:
                print("Email invalid without dot!!!!")
        else:
            print("Email invalid without @ !!!!")
    return wrapper

def is_phone_valid(func):
    def wrapper(email, y, a, phone, b, c):
        if len(phone) == 13:
            func(email, y, a, phone, b, c)
        elif phone[0] != '+':
            print("Error!!! Invalid phone number. The number must start with + ")
        else:
            print("Error!!! Wrong number of digits in phone number")
    return wrapper

    return