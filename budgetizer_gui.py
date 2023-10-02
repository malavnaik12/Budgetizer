from budgetizer import budgetizer
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pdfparser import pdf_parser

class budgetizer_gui:
    def __init__(self):
        pass

    def find_pdf(self):
        self.find_pdf_file = filedialog.askopenfilename()
        if (len(self.find_pdf_file) > 0):
            split_filename = self.find_pdf_file.split("/")
            self.show_pdf_file = Label(self.expense_subframe1,text=split_filename[-1]).grid(row=2,column=0,sticky='nsew')
        
    def parse_pdf(self):
        parser_init = pdf_parser()
        transactions, month_range = parser_init.main(self.find_pdf_file)
        print(transactions)
        print(month_range)
    
    def categorize_pdf(self):
        pass
    
    def exec_aggregate(self):
        pass
    
    def exec_forecast(self):
        pass

    def exec_vendor_name_edit(self):
        pass

    def exec_add_vendor(self):
        pass

    def exec_add_category(self):
        pass

    def main(self):
        self.root = Tk()
        self.root.geometry("700x600")
        self.root.title("Budgetizer")
        self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        self.mainframe.grid(row=0,column=0,sticky='nsew')
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.style = ttk.Style()
        self.style.theme_use('winnative')
        # self.style.configure()
        
        self.notes = ttk.Notebook(self.root)
        self.notes.grid(row=0,column=0,sticky='nsew')
        
        self.expense_mainframe = ttk.Frame(self.notes,borderwidth=2,relief='sunken')
        self.notes.add(self.expense_mainframe, text='Expense')
        self.expense_mainframe.rowconfigure(0,weight=1)
        self.expense_mainframe.rowconfigure(1,weight=1)
        self.expense_mainframe.rowconfigure(2,weight=1)
        self.expense_mainframe.rowconfigure(3,weight=1)
        self.expense_mainframe.rowconfigure(4,weight=1)
        self.expense_mainframe.rowconfigure(5,weight=1)
        self.expense_mainframe.rowconfigure(6,weight=1)
        self.expense_mainframe.columnconfigure(0,weight=1)
        self.expense_mainframe.columnconfigure(1,weight=4)
        self.expense_mainframe.columnconfigure(2,weight=1)

        self.expense_subframe1 = ttk.Frame(self.expense_mainframe,borderwidth=2,relief='sunken')
        self.expense_subframe1.grid(row=0,column=0,sticky='nsew',rowspan=10)
        self.expense_label1 = Label(self.expense_subframe1, text='PDF Processing Options', anchor='w',font=("Helvetica 12"))
        self.expense_label1.grid(row=0,column=0,sticky='nsew')
        self.expense_pdf_loc_button = ttk.Button(self.expense_subframe1, text="Input PDF", padding='5',command=self.find_pdf).grid(row=1,column=0,sticky='nsew')
        self.parse_expenses = ttk.Button(self.expense_subframe1, text="Parse PDF", command=self.parse_pdf).grid(row=3,column=0,sticky='nsew')
        self.catergorize_expenses = ttk.Button(self.expense_subframe1, text="Categorize PDF", command=self.categorize_pdf).grid(row=4,column=0,sticky='nsew')
        self.aggregate_expenses = ttk.Button(self.expense_subframe1, text="Add to Yearly Total", command=self.exec_aggregate).grid(row=5,column=0,sticky='nsew')
        self.forecast_expenses = ttk.Button(self.expense_subframe1, text="Forecast Expenses", command=self.exec_forecast).grid(row=6,column=0,sticky='nsew')

        self.expense_subframe2 = ttk.Frame(self.expense_mainframe,borderwidth=2,relief='sunken')
        self.expense_subframe2.grid(row=0,column=1,sticky='nsew',rowspan=10)
        self.expense_label2 = Label(self.expense_subframe2, text='Categorized list of Imported PDF Content', anchor='w',font=("Helvetica 12"))
        self.expense_label2.grid(row=0,column=0,sticky='nsew')
        self.expense_list = Listbox(self.expense_subframe2,height=25).grid(row=2,column=0,sticky='nsew')
        
        self.expense_subframe3 = ttk.Frame(self.expense_mainframe,borderwidth=2,relief='sunken')
        self.expense_subframe3.grid(row=0,column=2,sticky='nsew',rowspan=10)
        self.expense_label3 = Label(self.expense_subframe3, text='Misc. Options', anchor='w',font=("Helvetica 12"))
        self.expense_label3.grid(row=0,column=0,sticky='nsew')
        self.edit_vendor_name = ttk.Button(self.expense_subframe3, text="Edit Vendor Name", command=self.exec_vendor_name_edit).grid(row=2,column=0,sticky='nsew')

        self.add_vendor_entry = ttk.Button(self.expense_subframe3, text="Add Vendor", command=self.exec_add_vendor).grid(row=3,column=0,sticky='nsew')
        self.add_category = ttk.Button(self.expense_subframe3, text="Add Category", command=self.exec_add_category).grid(row=4,column=0,sticky='nsew')
        
        # for child in self.expense_mainframe.winfo_children(): 
        #     child.grid_configure(padx=5, pady=5)

        self.income_mainframe = ttk.Frame(self.notes,borderwidth=2,relief='sunken')
        self.notes.add(self.income_mainframe, text='Income')
        label2 = Label(self.income_mainframe, text='Incomes live here',font=("Helvetica 20 bold"))
        label2.grid(row=0,column=0,sticky='nsew')
        
        self.aggregate_mainframe = ttk.Frame(self.notes,borderwidth=2,relief='sunken')
        self.notes.add(self.aggregate_mainframe, text='Aggregate')
        label3 = Label(self.aggregate_mainframe, text='Aggregates live here',font=("Helvetica 20 bold"))
        label3.grid(row=0,column=0,sticky='nsew')
        
        self.forecast_mainframe = ttk.Frame(self.notes,borderwidth=2,relief='sunken')
        self.notes.add(self.forecast_mainframe, text='Forecast')
        label4 = Label(self.forecast_mainframe, text='Forecasts live here',font=("Helvetica 20 bold"))
        label4.grid(row=0,column=0,sticky='nsew')

        self.root.mainloop()
if __name__ == "__main__":
    class_init = budgetizer_gui()
    class_init.main()