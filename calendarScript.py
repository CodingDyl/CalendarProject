import calendar
from tkinter import *

#creating function to display calendar
def showCalendar():
    root = Tk()
    root.config(background='grey')
    root.title('Calendar for the year')
    root.geometry("550x600")

    year = int(year_field.get())
    gui_content = calendar.calendar(year)

    #creating labels
    calYear = Label(root, text=gui_content, font=("Consolas", 10, "bold"))
    calYear.grid(row=5, column=1, padx=20)

    root.mainloop()

def close():
    new.quit()

#driver code
if __name__ == '__main__':
    new = Tk()
    new.config(background='grey')
    new.title("Calendar")
    new.geometry("250x140")
    
    #creating labels
    cal = Label(new, text="Calendar", bg="grey", font=('Times', 28, 'bold'))
    #label for entering the year
    year = Label(new, text="Enter Year", bg='dark grey')
    #textbox
    year_field = Entry(new)
    #button
    button = Button(new, text= "Show Calendar", fg='Black', bg="Blue", command=showCalendar)
    btn_Exit = Button(new, text="Exit", fg='Black', bg='Blue', command=close)

    #setting widgets in position
    cal.grid(row=1, column=1)
    year.grid(row=2, column=1)
    year_field.grid(row=3, column=1)
    button.grid(row=4, column=1)
    btn_Exit.grid(row=6, column=1)
    new.mainloop()
