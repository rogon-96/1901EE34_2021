#My rollno is 1901EE34 Name:M D Midhun Reddy

import os
from openpyxl import Workbook,load_workbook
import pandas as pd
                                                                                   
def make_map(iterable,key_params,value_params,obj):                      #created_maps
    for index in range(len(iterable)):
        temp_row = iterable.iloc[index]
        key_list = temp_row.get(key_params[-1]) if len(key_params)==1 else tuple(temp_row.get(key) for key in key_params)
        values_list = temp_row.get(value_params[-1]) if len(value_params)==1 else [temp_row.get(key) for key in value_params]
        obj[key_list] = values_list
    return obj

def feedback_not_submitted():
    output_file_name = "course_feedback_remaining.xlsx"
    course_feedback = pd.read_csv("course_feedback_submitted_by_students.csv")
    course_info = pd.read_csv("course_master_dont_open_in_excel.csv")
    course_register = pd.read_csv("course_registered_by_all_students.csv")
    student_info = pd.read_csv("studentinfo.csv")

    course_feedback_dict = make_map(course_feedback,["stud_roll","course_code","feedback_type"],["id"],{})
    course_info_dict = make_map(course_info,['subno'],["ltp"],{})
    student_info_dict = make_map(student_info,["Roll No"],["Name","email","aemail","contact"],{})

    wb = Workbook()            
    ws = wb.active  
    ws.append(["rollno","register_sem","schedule_sem","subno","Name","email","aemail","contact"])

    for index in range(len(course_register)):                                                                                               
        temp_row = course_register.iloc[index]                               #getting every row
        rollno,subno,register_sem,schedule_sem= temp_row['rollno'],temp_row['subno'],temp_row['register_sem'],temp_row['schedule_sem']
        ltp_list= course_info_dict.get(subno).split('-')                #getting ltp details for courses                                                       
        for ind,ltp in enumerate(ltp_list):
            if ltp!='0' and (rollno,subno,ind+1) not in course_feedback_dict:       # condition for not submitted feedback
                stud_info = student_info_dict.get(rollno) if rollno in student_info_dict else ["NA_IN_STUDENTINFO" for i in range(0,4)] # for only
                register_info = [rollno,register_sem,schedule_sem,subno]
                ws.append(register_info+stud_info)                                                       
                break
    wb.save('./{}'.format(output_file_name))
    return
feedback_not_submitted()



