import xlrd, xlwt

oba = xlrd.open_workbook('oba.xlsx')
oba_data = oba.sheet_by_index(0)
print(oba_data.nrows)
buffer = ''
oba_loc = []
for i in range(oba_data.nrows):
    #print(oba_data.cell_value(i, 0))
    loc = oba_data.cell_value(i, 0)
    if  loc != '':
        buffer = loc
    oba_loc.append(buffer)
#print(oba_loc)

f_book = xlwt.Workbook()
f_sheet = f_book.add_sheet('1')

for i in range(len(oba_loc)):
    f_sheet.write(i, 0, oba_loc[i])

f_book.save('1.xls')