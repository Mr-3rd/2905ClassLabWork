def validate_birthday_month(input_value):
    month_dictionary = {
        "jan": "January", "feb": "February", "mar": "March",
        "apr": "April", "may": "May", "jun": "June",
        "jul": "July", "aug": "August", "sep": "September",
        "oct": "October", "nov": "November", "dec": "December"
    }

    if isinstance(input_value, int) and 1 <= input_value <= 12:
        return True, month_dictionary[input_value]["full"], month_dictionary[input_value]["abbreviated"]
    elif isinstance(input_value, str):
        input_value = input_value.lower()
        if input_value.isdigit():
            month_num = int(input_value)
            if 1 <= month_num <= 12:
                return True, month_dictionary[month_num]["full"], month_dictionary[month_num]["abbreviated"]

        if input_value in month_dictionary:
            return True, month_dictionary[input_value]["full"], month_dictionary[input_value]["abbreviated"]

    return False, None, None


# Example usage
user_input = input("Enter the birthday month (e.g., Jan, January, 1): ")
valid, full_name, abbreviated_name = validate_birthday_month(user_input)

if valid:
    print("Valid birthday month!")
    print("Full name:", full_name)
    print("Abbreviated name:", abbreviated_name)
else:
    print("Invalid input. Please enter a valid month abbreviation, full name, or integer between 1 and 12.")