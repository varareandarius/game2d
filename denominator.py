
def highest_denominator(first_number, second_number):
    if first_number == 0 or second_number == 0:
        return "Denominator is 0, so the division is not possible"
    else:
        # we need to find the highest common denominator usind first and second number
        while second_number:
            first_number, second_number = second_number, first_number % second_number
        if(first_number < 0):
            first_number = -first_number
        return first_number