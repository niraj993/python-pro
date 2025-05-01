from datetime import date



def reverse_str(string:str):
    return string[::-1]


def convert_list_into_str(array:list)->str:
    empty_str = ""
    for i in range(0,len(array)):
        empty_str += str(array[i])+ " ' "
    return empty_str

 
def check_sub_string(string:str,substr:str)->bool:
    new_str = string.split()
    if substr in new_str:
        return True
    return False



def extract_last_didgit(num:int):
    l = []
    while num > 0:
        l.append(num % 10)
        num = num // 10
    return l


def count_of_given_number(num:int):
    count = 0 
    while num >0:
        num = num // 10
        count += 1
    return count


def reverce_given_number(num:int)->list:
    rever_num = 0
    while num >0:
        last_digit = num %10
        rever_num = rever_num * 10 + last_digit
        num = num // 10
    return rever_num



def check_given_number_is_palimdrome(num:int)->bool:
    orig_num = num
    reverse_num = 0
    while num > 0:
        last_digit = num % 10
        reverse_num = reverse_num * 10 + last_digit
        num = num // 10
   
    return orig_num == reverse_num



def amstrong_num(num:int)->bool:
    original_num = num
    result = 0
    while num >0:
        last_digit = num%10
        result = result + last_digit * last_digit * last_digit
        num = num // 10

    return original_num == result


import math

def print_all_divisor(num:int)->list:
    l = []
    for i in range(1,num+1):
        if num % i == 0:
            l.append(i)
    return l



def check_prime_num(num:int):
    count = 0
    for n in range(1,num+1):
        if num % n == 0:
            count += 1
    print(count)
    return count == 2


def find_gcd_and_hcf(num1:int,num2:int)->list:
    highest_num = max(num1,num2)
    l = []
    for n in range(1,highest_num):
        if num1 % n == 0 and num2 % n == 0:
            l.append(n)
    return max(l)




def rev_string(string:str)->str:
    empty_str = ""
    for s in range(len(string)-1,-1,-1):
        empty_str += string[s]
    return empty_str
    

def check_given_string_palimdrone(string:str)->bool:
    original = string
    empty_str = ''
    for s in range(len(string)-1,-1,-1):
        empty_str += string[s]
    return empty_str == original


def count_vowel_and_cons(string:str)->int:
    vowel:str = "A, E, I, O, U"
    vowel_co:int = 0
    cons_co:int = 0 
    new_string:str = string.upper()
    for s in new_string:
        if s in vowel:
            vowel_co+=1
        else:
            cons_co+=1
    print("vowel is=============>",vowel_co)
    print("con count is ===============>",cons_co)
    

def factorial(num:int)->int:
    fact = 1
    for n in range(1,num+1):
        fact *= n
    return fact


def sum_natual_number(num:int)->int:
    add = 0 
    for n in range(1,num+1):
        add+=n
    return add


def check_prime_number(num:int)->bool:
    count = 0
    for n in range(1,num+1):
        if num % n ==0:
            count+=1
    return count == 2



def find_common_ele(l1:list,l2:list)->list:
    l = []
    for i in l1:
        for j in l2:
            if i in l2 and j in l1:
                l.append(j)
                
    return list(set(l))


def remove_duplicate(array:list)->list:
    empty_list = []
    for ele in array:
        if ele not in empty_list:
            empty_list.append(ele)
    return empty_list



def find_highest(array:list)->int:
    highest = array[0]
    for ele in array:
        if highest < ele:
            highest = ele
    return highest


def second_highest(array:list,pos)->int:
    if len(array) < 2:
        return "can't find second highest in this an array"
    new_array:list = list(set(array))
    new_array.sort(reverse=True)
    return new_array[pos]










print("result is ================>",second_highest([9,9,8,7,5,3,2],pos=2))

