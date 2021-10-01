 # grades_data = open("grades.csv", "r")
    # grades_list = [record.strip().split(",") for record in grades_data][1:]
    # c=1
    # for record in grades_list:
    #     if c==10:
    #         break 
    #     Roll,Sem_no, = record[0],record[1]
    #     file_path='./output/'+'{}.xlsx'.format(Roll)
    #     if not os.path.isfile(file_path):
    #         create_workbook(record) 
    #     wb=load_workbook(r'output\\{}.xlsx'.format(Roll))
    #     if not sheet_isexist(f'Sem{Sem_no}',wb):
    #         wb.create_sheet(f'Sem{Sem_no}',int(Sem_no))
    #         ws.column_dimensions['C'].width = max_length
    #     wb.active = int(Sem_no)
    #     ws = wb[f"Sem{int(Sem_no)}"]
    #     print(f"{c}Creating {Sem_no}")
    #     if ws.max_row==1 :
    #         ws.append(["Sl No.","Subject No.","Subject Name","L-T-P","Credit","Subject Type","Grade"])
    #     SubCode,Credit,Grade,Sub_Type = record[2:]
    #     subname,ltp,crd = course_dict[f"{SubCode}"][0],course_dict[f"{SubCode}"][1],course_dict[f"{SubCode}"][2]
    #     add_to_sheet(ws,[ws.max_row,SubCode,subname,ltp,crd,Sub_Type,Grade])
    #     wb.save(r'output\\{}.xlsx'.format(Roll))          
    #     c+=1;        