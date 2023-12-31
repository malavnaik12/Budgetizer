import tika;tika.initVM()
from tika import parser
import numpy as np
import os
import json

class pdf_parser:
    def __init__(self):
        self.month_range = []
        self.vendors = []
        self.values = []
        self.transactions = {}
        self.months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec']
    
    def inputs_func(self,pdf_loc):
        parsedPDF = parser.from_file(pdf_loc)
        self.split_list = parsedPDF['content'].split('\n\n')

    def extract_data(self):
        for line in self.split_list:
            first_letters = line[0:3]
            # print(line[0:6],line[-2:])
            if (('CR' in line[-2:]) or ('FROM' in line)):
                continue
            elif first_letters in self.months:
                if first_letters not in self.month_range:
                    self.month_range.append(first_letters)
                split_line = line.split(' ')
                self.vendors.append(split_line[4])

        for line in self.split_list:
            if (('CR' in line[-2:]) or ('FROM' in line)):
                continue
            try:
                float(line[0:4])
                cost_val = line
                self.values.append(cost_val)
            except:
                first_letters = line[0:3]
                if first_letters in self.months:
                    if first_letters not in self.month_range:
                        self.month_range.append(first_letters)
                    split_line = line.split(' ')
                    cost_val = split_line[-2]
                    try:
                        float(cost_val)
                        self.values.append(cost_val)
                    except:
                        continue
    def load_data(self, data_filename):
        os.makedirs(f"{self.file_loc}", exist_ok=True)
        with open(self.file_loc+data_filename, 'r') as file:
            return json.load(file)
    
    def save_data(self, data_filename, data):
        os.makedirs(f"{self.file_loc}", exist_ok=True)
        with open(self.file_loc+data_filename, 'w') as file:
            json.dump(data, file)

    def main(self,pdf_loc):
        self.inputs_func(pdf_loc)
        self.extract_data()
        self.values = self.values[1:]
        for item in range(0,len(self.values)):
            curr_vendor = self.vendors[item]
            if curr_vendor in self.transactions.keys():
                num = float(self.values[item])
                self.transactions[self.vendors[item]] += round(num,2)
            else:
                num = float(self.values[item])
                self.transactions[self.vendors[item]] = round(num,2)

        self.file_loc = f"./data/raw_data/{self.month_range[0]}_{self.month_range[1]}/"
        try:
            self.transactions = self.load_data("transactions.json")
        except:
            self.save_data("transactions.json",self.transactions)

        return self.transactions, self.month_range

if __name__ == "__main__":
    pdf_loc = "\\Users\\malav\\Downloads\\eStatement_2023-07-13.pdf"
    class_init = pdf_parser()
    transactions, _ = class_init.main(pdf_loc)
    print(transactions,len(transactions.keys()))