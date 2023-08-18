import tika
tika.initVM()
from tika import parser

class pdf_parser:
    def __init__(self):
        self.vendors = []
        self.values = []
        self.transactions = {}
    
    def inputs_func(self,pdf_loc):
        parsedPDF = parser.from_file(pdf_loc)
        self.split_list = parsedPDF['content'].split('\n\n')

    def extract_data(self):
        for line in self.split_list:
            first_letters = line[0:3]
            if 'FROM' in line:
                continue
            elif first_letters in ['Jul','Aug']:
                split_line = line.split(' ')
                self.vendors.append(split_line[4])

        for line in self.split_list:
            try:
                float(line[0:4])
                cost_val = line
                self.values.append(cost_val)
            except:
                first_letters = line[0:3]
                if 'FROM' in line:
                    continue
                elif first_letters in ['Jul','Aug']:
                    split_line = line.split(' ')
                    cost_val = split_line[-2]
                    try:
                        float(cost_val)
                        self.values.append(cost_val)
                    except:
                        continue

    def main(self,pdf_loc):
        self.inputs_func(pdf_loc)
        self.extract_data()

        self.values = self.values[1:]
        for item in range(0,len(self.vendors)):
            curr_vendor = self.vendors[item]
            if curr_vendor in self.transactions.keys():
                self.transactions[self.vendors[item]] += float(self.values[item])
            else:
                self.transactions[self.vendors[item]] = float(self.values[item])
        return self.transactions
# transactions["CANADA_WIDE_PARKING"] = transactions.pop("CANADA")
# transactions["LULULEMON"] = transactions.pop("LULULEMONCOM*")
if __name__ == "__main__":
    pdf_loc = "\\Users\\malav\\Downloads\\eStatement_2023-08-13.pdf"
    class_init = pdf_parser()
    transactions = class_init.main(pdf_loc)
    print(len(transactions.keys()))