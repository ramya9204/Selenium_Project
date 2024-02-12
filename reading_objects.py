import xlrd

path = r"C:\Users\HP\OneDrive\Desktop\locators_1.xlsx"

def read_locators():
    workbook = xlrd.open_workbook(path)
    worksheet_obj = workbook.sheet_by_name("locators_data")
    rows = worksheet_obj.get_rows()
    print(rows)
    header = next(rows)

    return {row[0].value : (row[1].value, row[2].value) for row in rows}

print(read_locators())