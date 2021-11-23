#My rollno is 1901EE34 Name:M D Midhun Reddy
import os
from openpyxl import Workbook,load_workbook
import pandas as pd
import numpy as np
def check_feedback(course_feedback_table,rollno,subno,ltp):
    check_list = [rollno,subno,ltp]
    try:
        course_feedback_table.loc[[check_list]]
    except:
        return True # returing true if feedback is not given .....same as below
    return False # returning false if feeback is given for a particular course and feedback_type
def feedback_not_submitted():
    print("please wait for 30 to 40 sec")
    output_file_name = "course_feedback_remaining.xlsx"
    course_feedback_table = pd.read_csv("course_feedback_submitted_by_students.csv")[["stud_roll","course_code","feedback_type","id"]].set_index(["stud_roll","course_code","feedback_type"])
    course_info_table = pd.read_csv("course_master_dont_open_in_excel.csv")[["subno","ltp"]].set_index('subno')
    course_register = pd.read_csv("course_registered_by_all_students.csv")[["rollno","register_sem","schedule_sem","subno"]]
    studentinfo = pd.read_csv("studentinfo.csv")[["Name","Roll No","email","aemail","contact"]].drop_duplicates(subset=['Roll No'],keep='first').set_index(["Roll No"])
    # took only necesaary values from the data


    #checking if the xlsx sheets exists or not
    if os.path.exists(output_file_name):
        wb = load_workbook(r"./{}".format(output_file_name))
    else:
        wb=Workbook()
        ws = wb.active
        ws.append(["rollno","register_sem","schedule_sem","subno","Name","email","aemail","contact"]) 
    ws=wb.active     
    # iterating through course_register 
    for ind,row in course_register.iterrows():
        rollno,subno= row['rollno'],row['subno']
        # print(rollno,subno)
        ltp_list= course_info_table.loc[f"{subno}"]["ltp"].split('-') #getting bits 
        ltp_list = [1 if x!='0' else 0 for x in ltp_list] #setting bits if the value is not '0'
        for index,ltp in enumerate(ltp_list):
            if ltp and check_feedback(course_feedback_table,rollno,subno,index+1): #checking feedback is exists or not 
                # print(rollno,subno)
                try: # getting student info 
                    stud_info = studentinfo.loc[f"{rollno}"]
                except:  #for somerollnumbers there are no details in student_info
                    stud_info = ["NA_IN_STUDENTINFO" for i in range(0,4)]
                final = np.concatenate((row,stud_info))
                ws.append(list(final)) #appending to worksheet
                break
    wb.save("./{}".format(output_file_name)) #saving the worksheet
    print("Created Succesfully")
    # i think worksheet is jumbled i.e 1901CE05 can be found in middle
    return
feedback_not_submitted()