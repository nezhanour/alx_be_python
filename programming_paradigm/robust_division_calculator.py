def safe_divide(numerator, denominator):
    #Division by Zero: Used a try-except block to catch ZeroDivisionError.
    try:
        float(numerator) / float(denominator)
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
    else:
        return f"The result of the division is {float(numerator) / float(denominator)}"
