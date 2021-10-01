import os
from openpyxl import Workbook
from openpyxl import load_workbook
import csv
def create_workbook(record):
    wb=Workbook()
    ws=wb.active
    ws.title = "Overall"
    wb.save(f'output\\{record[0]}.xlsx')
    return

def sheet_isexist(sheet_name,wb):
    for sheet in wb.sheetnames:
        if sheet == sheet_name:
            return 1
    return 0

def generate_marksheet():
    dir_name =  "output"
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    course_data = open("subjects_master.csv", "r")
    course_csv=csv.reader(course_data)
    course_list =  [list(record) for record in course_csv][1:] 
    course_dict = {}
    max_length = 0
    for record in course_list:
        subno = record[0]
        if subno not in course_dict:
            course_dict[subno] = record[1:]
            max_length = max(max_length,len(record[1]))  
    grades_data = open("grades.csv", "r")
    grades_csv = csv.reader(grades_data)
    grades_list = [list(record) for record in grades_csv][1:] 
    c=1
    for record in grades_list:
        Roll,Sem_no, = record[0],record[1]
        file_path='./output/'+'{}.xlsx'.format(Roll)
        if not os.path.isfile(file_path):
            create_workbook(record) 
        wb=load_workbook(r'output\\{}.xlsx'.format(Roll))
        if not sheet_isexist(f'Sem{Sem_no}',wb):
            wb.create_sheet(f'Sem{Sem_no}',int(Sem_no))
            ws = wb[f"Sem{int(Sem_no)}"]
            ws.column_dimensions["C"].width = max_length
        ws = wb[f"Sem{int(Sem_no)}"]
        print(f"{c}Creating {Sem_no}")
        if ws.max_row==1 :
            ws.append(["Sl No.","Subject No.","Subject Name","L-T-P","Credit","Subject Type","Grade"])
        SubCode,Credit,Grade,Sub_Type = record[2:]
        subname,ltp,crd = course_dict[f"{SubCode}"][0],course_dict[f"{SubCode}"][1],course_dict[f"{SubCode}"][2]
        ws.append([ws.max_row,SubCode,subname,ltp,crd,Sub_Type,Grade])
        wb.save(r'output\\{}.xlsx'.format(Roll))          
        c+=1;        
    return
generate_marksheet()