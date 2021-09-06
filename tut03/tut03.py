import os

def output_individual_roll():
    if not os.path.exists("output_individual_roll"):
        os.mkdir("output_individual_roll")

    rollno_dict = {}
    data = open("regtable_old.csv", "r")
    data_list = [record.strip().split(",") for record in data][1:]

    for record in data_list:
        rollno,register_sem,schedule_sem,subno,grade1,date_of_entry1,grade2,date_of_entry2,sub_type = record
        if rollno not in rollno_dict:
            rollno_dict[rollno] = ["rollno,register_sem,subno,sub_type"]
        rollno_dict[rollno].append(",".join(elem for elem in [rollno,register_sem,subno,sub_type]))

    for rollno in rollno_dict:
        path = os.path.join("output_individual_roll", rollno + ".csv")
        open(path,"w").write("\n".join(elem for elem in rollno_dict[rollno]))

    return

def output_by_subject():
    if not os.path.exists("output_by_subject"):
        os.mkdir("output_by_subject")
    subno_dict= {}
    data = open("regtable_old.csv", "r")
    data_list = [record.strip().split(",") for record in data][1:]

    for record in data_list:
        rollno,register_sem,schedule_sem,subno,grade1,date_of_entry1,grade2,date_of_entry2,sub_type = record
        if subno not in subno_dict:
            subno_dict[subno] = ["rollno,register_sem,subno,sub_type"]
        subno_dict[subno].append(",".join(elem for elem in [rollno,register_sem,subno,sub_type]))

    for subno in subno_dict:
        path = os.path.join("output_by_subject", subno + ".csv")
        open(path,"w").write("\n".join(elem for elem in subno_dict[subno]))
    return

output_by_subject()
output_individual_roll()
    
    