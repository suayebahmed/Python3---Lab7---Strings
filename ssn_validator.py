# a | return True or False for valid separator
def is_valid_sep(s):
    if s == ' ' or s == '-' or s == '.':
        return True
    else:
        return False


# b | return True or False depending on SSN value
def is_valid_ssn(ssn):
    if ssn.isdigit() and len(ssn) == 9:
        return True
    elif len(ssn) == 11 and ssn[3] == ssn[6] and ssn[0:3].isdigit() and ssn[4:6].isdigit() and ssn[7:11].isdigit():
        if ssn[3] == '-' or ssn[3] == ' ' or ssn[3] == '.':
            return True
        else:
            return False
    else:
        return False


# c | suggest correction based on the correctness of the valid ssn and separator
def suggest_correction(ssn):
    if is_valid_ssn(ssn) and len(ssn) == 9:
        return None
    elif is_valid_ssn(ssn) and len(ssn) == 11:
        return ssn
    # 11 chr long ssn correction
    elif len(ssn) == 11 and ssn[0:3].isdigit() and ssn[4:6].isdigit() and ssn[7:11].isdigit():
        if is_valid_sep(ssn[3]) or is_valid_sep(ssn[6]):
            if is_valid_sep(ssn[3]):
                sep = ssn[3]
            else:
                sep = ssn[6]
            return ssn[0:3] + sep + ssn[4:6] + sep + ssn[7:11]
        elif not is_valid_sep(ssn[3]) and not is_valid_sep(ssn[6]):
            return ssn[0:3] + ssn[4:6] + ssn[7:11]
    # 10 chr long ssn correction
    elif len(ssn) == 10:
        if is_valid_sep(ssn[3]) or is_valid_sep(ssn[5]):
            if is_valid_sep(ssn[3]) and ssn[0:3].isdigit() and ssn[4:10].isdigit():
                sep = ssn[3]
                return ssn[0:3] + sep + ssn[4:6] + sep + ssn[6:10]
            elif is_valid_sep(ssn[5]) and ssn[0:5].isdigit() and ssn[6:10].isdigit():
                sep = ssn[5]
                return ssn[0:3] + sep + ssn[3:5] + sep + ssn[6:10]
        elif not is_valid_sep(ssn[3]) and not is_valid_sep(ssn[5]):
            if not is_valid_sep(ssn[3]) and not ssn[3].isdigit():
                return ssn[0:3] + ssn[4:10]
            elif not is_valid_sep(ssn[5]) and not ssn[5].isdigit():
                return ssn[0:5] + ssn[6:10]
    else:
        return None


# d | repeatedly take user input and return valid or invalid. If invalid, return suggestion. X to exit
user_input = input('Enter an SSN (X to exit): ')
while user_input != 'X' or user_input != 'x':
    if user_input == 'X' or user_input == 'x':
        print('Thanks, come back soon!')
        break
    else:
        valid_invalid = is_valid_ssn(user_input)
        if valid_invalid:
            print('Valid')
        elif suggest_correction(user_input) is None:
            print('Invalid')
        else:
            print(f'Invalid, but maybe you meant {suggest_correction(user_input)}?')
        user_input = input('Enter an SSN (X to exit): ')
        continue
