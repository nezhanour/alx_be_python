from datetime import datetime
from datetime import timedelta

def display_current_datetime():
    current_date = datetime.now()
    dat_format = current_date.strftime("%Y-%m-%d %H:%M:%S")

    #print("Current date and time: ",dat_format )
    return dat_format

print("Current date and time: ",display_current_datetime())

number_of_days = int(input("enter a number of days (as an integer): "))
def calculate_future_date():
    future_date = datetime.today()
    future_date += timedelta(number_of_days)
    return future_date.strftime("%Y-%m-%d")

print("Future date: ", calculate_future_date())

