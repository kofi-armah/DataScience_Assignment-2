from datetime import datetime
import csv
from datetime import timedelta
# import Tkinter
from tkinter import *
root = Tk()


myLabel1 = Label(root, text="Welcome to today's daily work timer.")
myLabel2 = Label(root, text="Kindly choose a number")
myLabel3 = Label(root, text="1. Start timer")
myLabel4 = Label(root, text="2. Check wages for current task")
myLabel5 = Label(root, text="3. Exit program")

myLabel1.pack()
myLabel2.pack()
myLabel3.pack()
myLabel4.pack()
myLabel5.pack()

e = Entry(root)
e.pack()


def myClick():
    if e.get() == 1:
        start_time = datetime.now()
        myLabel6 = Label(root, text=start_time.strftime("\nStarting time is : %X"))
        myLabel7 = Label(root, text=start_time.strftime("\nTime : %H:%M"))
        myLabel8 = Label(root, text="Kindly enter  a number to stop the timer")
        myLabel6.pack()
        myLabel7.pack()
        myLabel8.pack()
        f = Entry(root)
        f.pack()
        end_time = datetime.now()
        myLabel9 = Label(root, text=end_time.strftime("\nEnding time is : %X"))
        myLabel10 = Label(root, text=end_time.strftime("\nTime : %H:%M)"))
        myLabel9.pack()
        myLabel10.pack()
        # time difference calculation
        t = (end_time - start_time)
        secs = t.seconds
        minutes = ((secs/60)%60)/60.0
        hours = secs/3600
        total_hours = round(hours + minutes, 2)
        # wage calculation (difference *5, result in $)
        employee_wage = total_hours*5
        # add append to file
        with open('nana_employee_wages.csv', 'a') as newFile:
            newFileWriter = csv.writer(newFile)
            newFileWriter.writerow(['Start date', 'Start time', 'End date', 'End time ', 'Total hour ', 'Pay'])
            newFileWriter.writerow([start_time.strftime("%x"), start_time.strftime("%H:%M%p"), end_time.strftime("%x"), end_time.strftime("%H:%M%p"), total_hours, f"$ {employee_wage}"])
        myLabel11 = Label(root, text="This work session was successfully added\n\n")
        myLabel12 = Label(root, text="\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n")
        myLabel11.pack()
        myLabel12.pack()
        myClick()
    elif e == 2:
        myLabel13 = Label(root, text="\nKindly check your file named 'employee_wages.csv' for your wages for your current task. Thank you.")
        myLabel13.pack()
        myClick()
    elif e == 3:
        myLabel14 = Label(root, text="\nThanks for using this program. See you soon.")
        myLabel14.pack()
        exit()
    else:
        myLabel15 = Label(root, text='\nSorry, you entered an invalid choice. Kindly try again.')
        myLabel15.pack()
        # myClick()


myButton = Button(root, text="Click", command=myClick())
myButton.pack()

# if __myClick__ == "__myClick__":
myClick()
