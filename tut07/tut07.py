#My rollno is 1901EE34 Name:M D Midhun Reddy

import os
from openpyxl import Workbook,load_workbook
import pandas as pd

def check_feedback(course_feedback_table,rollno,subno,ltp):
    check_list = [rollno,subno,ltp]
    try:
        course_feedback_table.loc[[check_list]]
    except:
        return True                                                                                 # returing true if feedback is not given .....same as below
    return False                                                                                    # returning false if feeback is given for a particular course and feedback_type

def feedback_not_submitted():
    output_file_name = "course_feedback_remaining.xlsx"
    course_feedback_table = pd.read_csv("course_feedback_submitted_by_students.csv")[["stud_roll","course_code","feedback_type","id"]].set_index(["stud_roll","course_code","feedback_type"])
    course_info_table = pd.read_csv("course_master_dont_open_in_excel.csv")[["subno","ltp"]].set_index('subno')
    course_register = pd.read_csv("course_registered_by_all_students.csv")[["rollno","register_sem","schedule_sem","subno"]]
    studentinfo = pd.read_csv("studentinfo.csv")[["Name","Roll No","email","aemail","contact"]].drop_duplicates(subset=['Roll No'],keep='first').set_index(["Roll No"])

    wb = Workbook()            
    ws = wb.active  
    ws.append(["rollno","register_sem","schedule_sem","subno","Name","email","aemail","contact"])

    for ind,row in course_register.iterrows():                                                           # iterating through course_register 
        rollno,subno= row['rollno'],row['subno']
        ltp_list= course_info_table.loc[f"{subno}"]["ltp"].split('-')                                    #getting bits 
        for index,ltp in enumerate(ltp_list):
            if ltp!='0' and check_feedback(course_feedback_table,rollno,subno,index+1):                  #checking feedback is exists or not 
                try:                                                                                     # getting student info 
                    stud_info = studentinfo.loc[f"{rollno}"]
                except:                                                                                  #for somerollnumbers there are no details in student_info
                    stud_info = ["NA_IN_STUDENTINFO" for i in range(0,4)]
                ws.append(list(row)+list(stud_info))                                                        #append ing to worksheet
                break
    wb.save('./{}'.format(output_file_name))
    print("Created Succesfully")
    return
feedback_not_submitted()

