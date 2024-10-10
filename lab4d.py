#!/usr/bin/env python3

def first_five(string):
    return string[:5]  # Return the first 5 characters

def last_seven(string):
    return string[-7:]  # Return the last 7 characters

def middle_number(num):
    num_str = str(num)
    return num_str[1:3]  # Return the 2nd and 3rd digits

def first_three_last_three(str1, str2):
    return str1[:3] + str2[-3:]  # Combine first 3 of str1 and last 3 of str2

if __name__ == '__main__':
    str1 = 'Hello World!!'
    str2 = 'Seneca College'
    num1 = 1500
    num2 = 1.50
    
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))
