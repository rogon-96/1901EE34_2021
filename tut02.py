
def get_memory_score(input_nums):
    check_list = list(filter(lambda x : type(x)!=int,input_nums))
    if len(check_list):
        print("Please enter a valid input_list.Invalid inputs detected :{}".format(check_list))
        return 
    list1 = []
    score=0
    for num in input_nums :
        if(num in list1):
            score+=1
        else:
            list1.append(num)
        if(len(list1)>5):
            list1.pop(0)
    print("Score: {}".format(score))
    return 

input_nums = [7, 5, 8, 6, 3, 5, 9, 7, 9, 7, 5, 6, 4, 1, 7, 4, 6, 5, 8, 9, 4, 8, 3, 0, 3]
get_memory_score(input_nums)

