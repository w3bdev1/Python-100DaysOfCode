def format_name(first_name, last_name):
    if first_name == "" or last_name == "":
        return "Invalid inputs"
    return first_name.title() + ' ' + last_name.title()

print(format_name("sudEEP", "BISWAS"))
print(format_name("sudEEP", ""))