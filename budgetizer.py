from categorizer import categorizer, initDict_expenses
import os, json

class budgetizer:
    def __init__(self):
        pass

    def load_data(self, data_filename):
        os.makedirs(f"{self.file_loc}", exist_ok=True)
        with open(self.file_loc+data_filename, 'r') as file:
            return json.load(file)
        
    def save_data(self, data_filename, data):
        # def serialize_sets(obj):
        #     if isinstance(obj, set):
        #         return list(obj)
        #     return obj
        os.makedirs(f"{self.file_loc}", exist_ok=True)
        with open(self.file_loc+data_filename, 'w') as file:
            json.dump(data, file)

    def main(self, pdf_loc):
        self.file_loc = f"./data/global_data/"
        try:
            global_cat_vendors = self.load_data("vendors.json")
            global_cat_values = self.load_data("values.json")
        except:
            global_cat_vendors = initDict_expenses()
            global_cat_values = initDict_expenses()
            cater = categorizer()
            vendors, values = cater.categorize(pdf_loc=pdf_loc)
            for key in vendors.keys():
                if vendors[key] != 0:
                    if type(global_cat_vendors[key]) is int:
                        global_cat_vendors[key] = []
                    #     global_cat_vendors[key] = set()
                    # global_cat_vendors[key] = set(global_cat_vendors[key])
                    global_cat_vendors[key].append(vendors[key])
            for key in values.keys():
                if values[key] != 0:
                    global_cat_values[key] += values[key]
            self.save_data("vendors.json",global_cat_vendors)
            self.save_data("values.json",global_cat_values)
        for key in global_cat_values.keys():
            print(key,global_cat_vendors[key],global_cat_values[key])

if __name__ == "__main__":
    pdf_loc = "\\Users\\malav\\Downloads\\eStatement_2023-07-13.pdf"
    class_init = budgetizer()
    class_init.main(pdf_loc)