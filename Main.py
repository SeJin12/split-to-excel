from openpyxl import Workbook

def makeExcelFile(columns, data, fileIndex):
    workbook = Workbook()
    sheet = workbook.create_sheet('data')

    sheet = workbook.active
    sheet.append(columns)

    for d in data:
        sheet.append(d)

    workbook.save("./output"+ str(fileIndex) +".xlsx")
    return

f = open('./input.txt' ,'r', encoding="utf8")

index = -3;
targetCount = 0
columns = []
data = []
fileIndex = 1

targetCount = int(f.readline())
columns = f.readline().split("\t")

while True:
    line = f.readline()
    
    if not line: break
    
    data.append(line.split("\t"))
    if(len(data) == targetCount):
        makeExcelFile(columns, data, fileIndex)
        fileIndex += 1
        data.clear()
f.close()

if len(data) > 0 :
    # 나머지 엑셀 다운로드
    makeExcelFile(columns, data, fileIndex)
    data.clear()