n = 45637




reversed_string = ""
while n > 0:
    remainder = n % 10
    reversed_string = reversed_string + str(remainder) 
    print(reversed_string )
    n = n // 10
    print(n)
    print(reversed_string)

""" #     n = 12345
# reversed_num = 0

# while n > 0:
#     remainder = n % 10           # get last digit
#     reversed_num = reversed_num * 10 + remainder
#     n = n // 10                  # remove last digit

# print("Reversed number is:", reversed_num) """

    

