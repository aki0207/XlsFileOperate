import xlwt

# xlwtだと新規にファイルを作成し、書き込むことはできるが
# 既存のファイルに書き込むことができない
# xlsファイルを作成
book = xlwt.Workbook()
sheet1 = book.add_sheet('sheet2')

sheet1.write(0, 0, 100)
sheet1.write(0, 1, 200)
sheet1.write(1, 0, 300)
sheet1.write(1, 1, 400)

book.save('test.xls')