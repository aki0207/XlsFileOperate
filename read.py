import xlrd
# read.pyファイルと同一ディレクトリにxlaファイルを配置している場合

book = xlrd.open_workbook('test_xlrd.xls')

# endは改行しないために使われている
print("Sheet num: ", end='')
# シートの数出力
print(book.nsheets)

# シート名出力
for name in book.sheet_names():
    print(name)

# インデックスで指定
print("index: " + book.sheet_by_index(0).name)
# シート名で指定
print("name: " + book.sheet_by_name('Sheet1').name)

s1 = book.sheet_by_index(0)
print("sheet1,B3: ",s1.cell(2,1).value)