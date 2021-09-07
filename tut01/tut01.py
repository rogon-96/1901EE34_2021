def meraki_helper(n):
    prev = n % 10
    num = n//10
    while(num):                                  # checking until the number is greater than 0
        r = num % 10
        if(abs(r-prev) != 1):
            print("No-{} is Not a Meraki number".format(n))
            return 0
        prev = r
        num //= 10
    print("Yes-{} is a Meraki number".format(n))
    return 1

input_list = [12, 14, 56, 78, 98, 54, 678, 134,789, 0, 7, 5, 123, 45, 76345, 987654321]
count = 0
for item in input_list:
    count += meraki_helper(item)        # calling function for every number in list
print("The input_list contains {} meraki numbers and {} non meraki numbers".format(count, len(input_list)-count))
