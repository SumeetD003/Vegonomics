import openpyxl

def get_maximum_rows(*, sheet_object):
    rows = 0
    for max_row, row in enumerate(sheet_object, 1):
        if not all(col.value is None for col in row):
            rows += 1
    return rows

wb = openpyxl.load_workbook('Dataset.xlsx')
sheet=wb.active

rows=get_maximum_rows(sheet_object=sheet)
for i in range(2,rows+1):
    st=str(sheet['A'+str(i)].value).lower()
    l=st.split()
    if("omelette" in l or "egg" in l or "chicken" in l):
        sheet['C'+str(i)]=1
    else:
        sheet['C'+str(i)]=0

wb.save('Dataset.xlsx')
wb.save('Dataset1.csv')