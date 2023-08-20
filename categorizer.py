from pdfparser import pdf_parser
import json
import os

class categorizer:
    def __init__(self):
        os.makedirs("./data/", exist_ok=True)
        try:
            self.categorized_expense_vendors = self.load_data('./data/expense_vendors.json')
            self.categorized_expense_values = self.load_data('./data/expense_values.json')
            self.categorized_income_vendors = self.load_data('./data/income_vendors.json')
            self.categorized_income_values = self.load_data('./data/income_values.json')
        except:
            self.categorized_expense_vendors = initDict_expenses()
            self.categorized_expense_values = initDict_expenses()
            self.categorized_income_vendors = initDict_income()
            self.categorized_income_values = initDict_income()
    
    def load_data(self, data_path):
        os.makedirs(f"./data/{self.statement_months[0]}_{self.statement_months[1]}/", exist_ok=True)
        with open(data_path, 'r') as file:
            return json.load(file)
        
    def save_data(self, data_path, data):
        os.makedirs(f"./data/{self.statement_months[0]}_{self.statement_months[1]}/", exist_ok=True)
        with open(data_path, 'w') as file:
            json.dump(data, file)

    def parse_pdf(self,pdf_loc):
        parser = pdf_parser()
        self.transactions, self.statement_months = parser.main(pdf_loc=pdf_loc)
        self.vendor_list = list(self.transactions.keys())
        self.categorize()

    def categorize(self):
        for vendor in self.vendor_list:
            # vendor_check = input(f"Would you like to edit this vendor name: {vendor}?\nPlease answer Yes or No (case-sensitive): ")
            # if vendor_check == 'Yes':
            #     new_vendor_name = input(f"Provide new name for {vendor} (case-sensitive): ")
            #     vendor = new_vendor_name
            print(f"Available Categories: {list(self.categorized_expense_vendors.keys())}")
            category = input(f"What is the category of this {vendor} (case-sensitive)? ")
            self.categorized_expense_values[category] += self.transactions[vendor]
            if ((len(str(self.categorized_expense_vendors[category])) == 1) and (type(self.categorized_expense_vendors[category]) == int)):
                self.categorized_expense_vendors.update({f"{category}":[f"{vendor}"]})
            else:
                if vendor not in list(self.categorized_expense_vendors[category]):
                    self.categorized_expense_vendors[category].append(vendor)
            print(self.categorized_expense_vendors[category],self.categorized_expense_values[category])

class initDict_expenses(dict):
    _keys = ['Rental','Health','Groceries','Take-out','Travel','Car','Electricity','Internet','Natural Gas','Other',
            'Clothes','Furniture','Water','Loans','TFSA','RRSP','FHSA','Self-Improvement','Borrowed Money','Montreal']
    def __init__(self, valtype=int):
        for key in initDict_expenses._keys:
            self[key] = valtype()

class initDict_income(dict):
    _keys = ['Pay','Tax Return','Govt Rebate','Insurance','CC Rebate','Goods Returns','Mom']
    def __init__(self, valtype=int):
        for key in initDict_income._keys:
            self[key] = valtype()

if __name__ == "__main__":
    pdf_loc = "\\Users\\malav\\Downloads\\eStatement_2023-07-13.pdf"
    class_init = categorizer()
    transactions = class_init.parse_pdf(pdf_loc)