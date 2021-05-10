from datetime import datetime
import csv
from datetime import timedelta
# import Tkinter
from tkinter import *

root = Tk()


def main():
    print("\nHi Welcome to daily work timer.")
    # print("\nKindly choose a number:"
    # "\n 1. Start timer"
    # "\n 2. Check wages for current task"
    # "\n 3. Exit program")
    selection = int(input("\nWelcome to employee daily wage timer:"
                          "\n 1. Start timer"
                          "\n 2. Check wages for current task"
                          "\n 3. Exit program: "))

    if selection == 1:
        start_time = datetime.now()
        print(start_time.strftime("\nStarting time is : %X"))
        # print("Kindly enter a number to stop the timer")
        stop = int(input("Kindly enter a number to stop the timer: "))
        end_time = datetime.now()
        print(end_time.strftime("\nEnding time is : %X"))
        print(end_time.strftime("\nTime : %H:%M)"))
        # time difference calculation
        t = (end_time - start_time)
        secs = t.seconds
        minutes = ((secs / 60) % 60) / 60.0
        hours = secs / 3600
        total_hours = round(hours + minutes, 2)
        # wage calculation (difference *5, result in $)
        employee_wage = total_hours * 5
        # add append to file
        with open('employee_daily_wage.csv', 'a') as newFile:
            newFileWriter = csv.writer(newFile)
            newFileWriter.writerow(['Start date', 'Start time', 'End date', 'End time ', 'Total hour ', 'Pay'])
            newFileWriter.writerow([start_time.strftime("%x"), start_time.strftime("%H:%M%p"), end_time.strftime("%x"),
                                    end_time.strftime("%H:%M%p"), total_hours, f"$ {employee_wage}"])
        print("This work session was successfully added\n\n")
        print("\nThanks for using our services\n")
        main()
    elif selection == 2:
        print("\nKindly check your file named 'employee_daily_wage.csv' "
              "\nfor your wages for your current task. Thank you.")
        main()
    elif selection == 3:
        print("\nThanks for using this program. See you soon.")
        exit()
    else:
        print('\nSorry, you entered and invalid choice. Kindly try again.')
        main()


if __name__ == "__main__":
    main()
