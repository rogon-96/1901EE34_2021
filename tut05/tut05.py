import os
from openpyxl import Workbook
from openpyxl import load_workbook
import csv
def create_workbook(record):
    wb=Workbook()
    ws=wb.active
    ws.title = "Overall"
    wb.save(f'output\\{record[0]}.xlsx')
    return wb

def sheet_isexist(sheet_name,wb):
    for sheet in wb.sheetnames:
        if sheet == sheet_name:
            return 1
    return 0

def get_credits_spi(wb,credit_map):
    Spi,Credits= [],[]
    for sheet in wb.sheetnames[1:]:
        ws = wb[sheet]
        credits = [int(cell.value) for cell in ws["E"][1:]]
        spi = [credit_map[cell.value.strip().strip("*")] for cell in ws["G"][1:]]
        Credits.append(sum(credits))
        Spi.append(round(sum([spi[i]*credits[i] for i in range(len(spi))])/sum(credits),2))
    return Spi,Credits

def get_results(Spi,ws,Credits):        
    ws.append(["Semester No"]+[x for x in range(1,9)])
    ws.append(["Semester wise Credit taken"]+Credits)
    ws.append(["SPI"]+Spi)
    prefix_credits = [sum(Credits[:i+1]) for i in range(len(Credits))]
    ws.append(["Total Credits taken"]+prefix_credits)
    CPI_num=[Spi[i]*Credits[i] for i in range(len(Credits))] 
    ws.append(["CPI"]+[round(sum(CPI_num[:i+1])/prefix_credits[i],2) for i in range(len(Spi))])
    return

def calculate_overallpage(wb,record,credit_map):
    name,Roll = record[1],record[0]
    ws =wb.active
    ws.column_dimensions["A"].width = 30
    ws.append(["RollNo",Roll])
    ws.append(["Name of Student",name])
    ws.append(["Discipline",Roll[4:6]])
    Spi,Credits= get_credits_spi(wb,credit_map)
    get_results(Spi,ws,Credits)
    return

def generate_marksheet():
    dir_name =  "output"
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)

    course_data = open("subjects_master.csv", "r")
    course_csv=csv.reader(course_data)
    course_list =  [list(record) for record in course_csv][1:] 

    grades_data = open("grades.csv", "r")
    grades_csv = csv.reader(grades_data)
    grades_list = [list(record) for record in grades_csv][1:] 

    credit_map = {'AA':10,'AB':9,'BB':8,'BC':7,'CC':6,'CD':5,'DD':4,'F':0,'I':0,
                'AA*':10,'AB*':9,'BB*':8,'BC*':7,'CC*':6,'CD*':5,'DD*':4,'F*':0,'I*':0}

    names_data = open("names-roll.csv","r")
    names_csv = csv.reader(names_data)
    names_list = [list(record) for record in names_csv]
    
    course_dict = {}
    max_length = 0

    for record in course_list:
        subno = record[0]
        if subno not in course_dict:
            course_dict[subno] = record[1:]
            max_length = max(max_length,len(record[1]))  
    c=1
    wb = 0
    for i in range(len(grades_list)):
        record = grades_list[i]
        if i+1 != len(grades_list):
            record1 = grades_list[i+1]
        Roll,Sem_no, = record[0],record[1]
        file_path='./output/'+'{}.xlsx'.format(Roll)
        if not os.path.isfile(file_path):
            wb = create_workbook(record) 
        if not sheet_isexist(f'Sem{Sem_no}',wb):
            wb.create_sheet(f'Sem{Sem_no}',int(Sem_no))
            ws = wb[f"Sem{int(Sem_no)}"]
            ws.column_dimensions["C"].width = max_length
        ws = wb[f"Sem{int(Sem_no)}"]
        print(f"Iterating {i+1} row")
        if ws.max_row==1 :
            ws.append(["Sl No.","Subject No.","Subject Name","L-T-P","Credit","Subject Type","Grade"])
        SubCode,Credit,Grade,Sub_Type = record[2:]
        subname,ltp,crd = course_dict[f"{SubCode}"][0],course_dict[f"{SubCode}"][1],course_dict[f"{SubCode}"][2]
        ws.append([ws.max_row,SubCode,subname,ltp,crd,Sub_Type,Grade])
        if i+1==len(grades_list) or record[0]!=record1[0] :
            calculate_overallpage(wb,names_list[c],credit_map)
            print(f"Calculating {c} student's result")
            wb.save(r'output\\{}.xlsx'.format(Roll))          
            c+=1;       
    return
generate_marksheet()