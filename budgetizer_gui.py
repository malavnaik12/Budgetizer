from budgetizer import budgetizer
from tkinter import *
from tkinter import ttk

class budgetizer_gui:
    def __init__(self):
        pass

    def main(self):
        self.root = Tk()
        self.root.geometry("700x600")
        self.root.title("Budgetizer")
        self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        self.mainframe.grid(row=0,column=0,sticky='nwes')
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        self.notes = ttk.Notebook(self.root)
        self.notes.grid(row=0,column=0,sticky='nwes')
        
        self.frame1 = ttk.Frame(self.notes)
        self.notes.add(self.frame1, text='Expense')
        label1 = Label(self.frame1, text='Expenses live here',font=("Helvetica 20 bold"))
        label1.grid(row=0,column=0,sticky='nwes')

        self.frame2 = ttk.Frame(self.notes)
        self.notes.add(self.frame2, text='Income')
        label2 = Label(self.frame2, text='Incomes live here',font=("Helvetica 20 bold"))
        label2.grid(row=0,column=0,sticky='nwes')
        
        self.frame3 = ttk.Frame(self.notes)
        self.notes.add(self.frame3, text='Aggregate')
        label3 = Label(self.frame3, text='Aggregates live here',font=("Helvetica 20 bold"))
        label3.grid(row=0,column=0,sticky='nwes')
        
        self.frame4 = ttk.Frame(self.notes)
        self.notes.add(self.frame4, text='Forecast')
        label4 = Label(self.frame4, text='Forecasts live here',font=("Helvetica 20 bold"))
        label4.grid(row=0,column=0,sticky='nwes')
        # self.root.option_add('*tearOff', FALSE)
        # self.win = Toplevel(self.root)
        # self.menubar = Menu(self.win)
        # self.win['menu'] = self.menubar
        # menu_expenses = 
        

        self.root.mainloop()
if __name__ == "__main__":
    class_init = budgetizer_gui()
    class_init.main()