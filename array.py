import ctypes
from typing import Any

class MeraList:
    def __init__(self)->None:
        self.array_size = 1
        self.number_of_item = 0
        self.array = self.__make_array(self.array_size)


    def __make_array(self,new_array_size:int):
        return (ctypes.py_object * new_array_size)()
    

    def __len__(self):
        return self.number_of_item
    
    def __resize(self,new_capacity):
        self.second_array = self.__make_array(new_array_size=new_capacity)
        self.array_size = new_capacity

        for ele in range(self.number_of_item):
            self.second_array[ele] = self.array[ele]
        self.array = self.second_array


    def __str__(self):
        empty_str = ""
        for ele in range(self.number_of_item):
            empty_str = empty_str + str(self.array[ele]) + ","
        return "[" + empty_str[:-1]+ "]"

    

    def append(self,new_item):
        if self.number_of_item == self.number_of_item:
            self.__resize(self.array_size*2)
        self.array[self.number_of_item]= new_item
        self.number_of_item = self.number_of_item+1


    def clear(self):
        self.number_of_item = 0 
        self.array_size = 0
    

    def __getitem__(self,index):
        for idx in range(self.number_of_item):
            if idx == index:
                return self.array[idx]
        raise IndexError("Out of range")
    
    
    def pop(self):
        if self.number_of_item == 0:
            return "Empty List"
        print(self.array[self.number_of_item-1])
        self.number_of_item = self.number_of_item - 1

        
    def find(self,item):
        for idx in range(self.number_of_item):
            if self.array[idx] == item:
                return idx
        raise ValueError(f"{item} not in List")
        
    

    def count(self,item):
        counter = 0
        for idx in range(self.number_of_item):
            if self.array[idx] == item:
                counter = counter + 1
        return counter
    

    def insert(self,pos:int,item:Any):
        if self.number_of_item == self.array_size:
            self.__resize(new_capacity=2)

        for idx in range(self.number_of_item,pos,-1):
            self.array[idx] = self.array[idx-1]
        self.array[pos] = item
        self.number_of_item = self.number_of_item + 1
 
    def __delitem__(self,pos:int):
        if pos < self.number_of_item:
            for idx in range(pos,self.number_of_item-1):
                self.array[idx] = self.array[idx+1]
            self.number_of_item = self.number_of_item - 1
        return -1


    def remove(self,item:Any):
        pos = self.find(item=item)
        if type(pos) == int:
            self.__delitem__(pos=pos)
        return pos




    

    


   

    

# mera_obj = MeraList()
# mera_obj.append(1)
# mera_obj.append(12)
# mera_obj.append(1)
# mera_obj.append(20)
# print(mera_obj)
# print(mera_obj.remove(item=123))
# print(mera_obj)

# Find the highest ele in the array

def find_highest_ele(array:list)->int:
    largest = array[0]
    for idx in range(0,len(array)):
        print(idx)
        if array[idx] > largest:
            largest = array[idx]
    return largest


# find the second highest
def find_second_largest(array:list)->int:
    largest = second_largest = float('-inf')
    for idx in range(0,len(array)):
        if array[idx] > largest:
            second_largest = largest
            largest = array[idx]
        elif array[idx] > second_largest and array[idx] != largest:
            second_largest = array[idx]

        
    
    return second_largest



# Check given array is sorted or Not
def check_array_is_sorted(array:list)->bool:
    for idx in range(0,len(array)):
        if array[idx] > array[idx-1]:
            flag = True
        else:
            flag = False
    return flag



# Remove duplicates from sorted an aray

def remove_duplicate_sorted_array(array:list)->list:
    empty_array = []
    for idx in range(0,len(array)):
        if array[idx] not in empty_array:
            empty_array.append(array[idx])
    return empty_array

def remove_duplicate_with_two_pointer(array:list)->list:
    index = 0
    for idx in range(0,len(array)):
        if array[idx] != array[index]:
            array[index+1] = array[idx]
            index+=1
    return index+1



# Left rotate an array first place in given array

def left_rotate(array:list)->list:
    temp = array[0]
    for idx in range(len(array)-1):
        print(idx)
        array[idx] = array[idx+1]
    array[-1] = temp
    return array

    

def left_rotate_the_array_by_D(array:list,d:int)->list:
    return array[d:] + array[:d] 


# we can solve this problem using reverse --> second option
def left_rotate_array_by_D_1(array:list,D:int)->list:
    temp_array = array[:D]
    print(temp_array)
    for idx in range(0,len(temp_array)):
        print(idx)
        array[idx] = array[idx+1]
    return array


# Move all zero in the last of an array
# array = [1,2,0,4,0,12,9,0]
# output should look like this -> [1,2,4,12,9,0,0,0]


# Broute force solution
def move_all_zero_in_last_of_array(array:list)->list:
    lenth_of_array = len(array)
    temp_array = []
    for idx in range(0,lenth_of_array):
        if array[idx] != 0:
            temp_array.append(array[idx])
    
    lenth_of_zero = lenth_of_array - len(temp_array)
    
    for _ in range(lenth_of_zero):
        temp_array.append(0)
    return temp_array

    


def linear_serach(array:list,n:int)->int:
    for idx in range(0,len(array)):
        if array[idx] == n:
            return idx
    return -1


# Find the union of given two sorted an array

def union_two_sorted_an_aaray(array_1:list,array_2:list)->list:
    return list(set(array_1) | set(array_2))



def union_two_sorted_arrays(array_1:list,array_2:list)->list:
    empty_array = []
    size_array_1 = len(array_1)
    size_array_2 = len(array_2)
    i=j=0
    while (i<size_array_1 and j<size_array_2):
        if array_1[i] < array_2[j]:
            empty_array.append(array_1[i])
            i+=1
        elif array_1[i] > array_2[j]:
            empty_array(array_2[j])
            j+=1

        else:
            empty_array.append(array_1[i])
            i+=1
            j+=1

    while i < size_array_1:
        empty_array.append(array_1[i])
        i+=1

    while j < size_array_2:
        empty_array.append(array_2[j])
        j+=1

    return empty_array



# Find the missing number of 1 to N in given number
# Broute force apporoach
def find_missing_number(array:list,n:int)->int:
    for n in range(n-1):
        for idx in range(0,len(array)):
            if array[idx] != n:
                missing_n = n

    return missing_n
        

#  better solution using hashing
# def find_missing_number_1()

# Optimal solution

def find_missing_number_1(array:list,num:int):
    add = 0
    for n in range(1,num+1):
        add += n
    return add-sum(array)


# Find max consective ones
# Optimal solulation

def find_max_consec_ones(array:list)->int:
    max_n = 0
    counter = 0
    for idx in range(0,len(array)):
        if array[idx] == 1:
            counter +=1
            max_n = max(max_n,counter)
        else:
            counter = 0
    return max_n


# Find the number that appears ones
# [1,2,3,4,5,6,6,5,4,3,2]

# Brute force solution
def find_the_number_appers_ones(array:list)->int:
    for i in range(0,len(array)):
        for j in range(0,len(array)):
            counter = 0
            if array[i] == array[i]:
                counter +=1
        if counter == 1:
            return array[i]
    return -1

# Better Solution
def find_the_number_appears_ones_better(array:list)->int:
    d = {}
    for ele in array:
        if ele not in d:
            d[ele] = 1
        else:
            d[ele] +=1
    for key in d:
        if d[key] == 1:
            return key
    return -1


# Find the longest subarray with sum k
# Brute force solution

def find_the_logest_sub_array_sum(array:list,k:int)->int:
    max_sum = float('-inf')
    result_dict = {}
    for i in range(0,len(array)):
        result = 0
        for j in range(i,len(array)):
            result+=array[j]
            result_dict[tuple(array[i:j+1])] = result
            # if result>max_sum:
            #     max_sum=result
    print(result_dict)
    for key in result_dict:
        if len(key) == k:
            return max(max_sum, result_dict[key])
    return -1




# Two Sum problem given an array and target chek target match or not or return index of an aaray
# Brute Force solution


def tow_sum_with_target(array:list,target:int)->int:
    for i in range(0,len(array)):
        for j in range(i+1,len(array)):
            if array[i] + array[j] == target:
                return "yes"
            
    return "Not"

# Better Solution
def tow_sum_with_target_1(array:list,target:int)->int:
    d= {}
    for idx in range(0,len(array)):
        num = array[idx]
        more = target - num
        if more in d:
            return "yes"
        else:
            d[array[idx]] = idx

    return "No"
    

# Optimal without hash data structure
def tow_sum_with_target_2(array:list,target:int)->str:
    left,right = 0,len(array)-1
    array.sort()
    while left<right:
        result = array[left] + array[right]
        if result == target:
            return "Yes"
        elif result < target:
            left +=1
        else:
            right -= 1
    return "No"
   

# Sort a given an array
# Broute Force Solution
def sort_an_array(array:list):
    count_1 = 0
    count_2 = 0
    count_3 = 0

    for idx in range(0,len(array)):
        if array[idx] == 0:
            count_1 +=1
        elif array[idx] == 1:
            count_2+=1
        elif array[idx] == 2:
            count_3 +=1
    for i in range(count_1):
        array[i] = 0
    
    for j in range(count_1,count_1+count_2):
        array[j] = 1
    for k in range(count_1 + count_2, len(array)):
        array[k] = 2
    return array


# Majority of given an array >n/2
# Broute Force
def majority_of_given_an_array(array: list):
    length_array = len(array)   
    for j in range(length_array):
        count = 0
        for k in range(length_array):
            if array[j] == array[k]:
                count += 1  
        if count > length_array // 2:  
            return array[j]
    return None   

# Better Solution
def majority_of_given_an_array_1(array:list):
    lenght_array = len(array)
    d = {}
    for idx in range(0,lenght_array):
        if array[idx] not in d:
            d[array[idx]] = 1
        else:
            d[array[idx]] +=1
    for key in d:
        if d[key] > lenght_array//2:
            return key
    return -1

# Maximum in subarray
# Better
def maximum_in_subarray(array:list):
    lenght_array = len(array)
    result_dict = {}
    for i in range(0,lenght_array):
        result = 0
        for j in range(i,lenght_array):
            result +=array[j]
            result_dict[tuple(array[i:j+1])] = result
    
    return result_dict[max(result_dict,key=result_dict.get)]

# Optimal solution with kadane's algo
def maximum_in_subarray_1(array:list):
    maxi = float('-inf')
    sum_array = 0
    for idx in range(0,len(array)):
        sum_array+= array[idx]

        if sum_array > maxi:
            maxi = sum_array

        if sum_array < 0:
            sum_array = 0
    return maxi

# Rearrange an array
# Broute Force solution
def rearrange_an_array(array:list):
    pos = []
    neg = []
    for ele in array:
        if ele < 0:
            pos.append(ele)
        else:
            neg.append(ele)
    


# Optimal solution in terms of space complixity
def rearrange_an_array_a(array:list):
    ans_array = [0] * len(array)
    positiveIndex = 0
    nagative_index = 1
    for ele in array:
        if ele < 0:
            ans_array[nagative_index] = ele
            nagative_index +=2
        else:
            ans_array[positiveIndex] = ele
            positiveIndex +=2
    return ans_array



# Generate next permutation 
# Brute force solution

from itertools import permutations

def generate_next_permutation(array: list):
    all_permutations = sorted(permutations(array))
    print(all_permutations)
    for i in range(len(all_permutations)):
        if list(all_permutations[i]) == array:
            if i + 1 < len(all_permutations):
                return list(all_permutations[i + 1])
            else:
                return list(all_permutations[0])   
    return array  # 


# Find Leaders an array
# Brute Force solution
def find_leader(array:list):
    empty_list = []
    for i in range(0,len(array)):
        for j in range(i+1,len(array)):
            if array[i] < array[j]:
                empty_list.append(array[j])
    return empty_list[:-1]


# Optimal Solution
def find_leader_1(array:list):
    maxi = float("-inf")
    ans_list = []
    for idx in range(len(array)-1,-1,-1):
        if array[idx] > maxi:
            ans_list.append(array[idx])
        maxi = max(maxi,array[idx])
    return ans_list



# Find Longest consecutive sequence 
# Brute force solutiuon
def find_longest_consecutive(array:list):
    longest = 0
    for idx in range(0,len(array)):
        n = array[idx]
        count = 1

        while n + 1 in array:
            n+=1
            count+=1
        longest = max(longest,count)

    return longest

    

# Better solution
def find_longest_consecutive_1(array: list) -> int:
    if not array:
        return 0   
    
    array = sorted(set(array))  #  
    longest, count = 1, 1  

    for i in range(1, len(array)):  
        if array[i] == array[i - 1] + 1:  
            count += 1  
            longest = max(longest, count)   
        else:
            count = 1   

    return longest



# Optimal solution
def find_longest_consecutive_optimal(array: list) -> int:
    if not array:
        return 0   

    longest = 1
    count = 1
    new_array = sorted(set(array))   

    for idx in range(1, len(new_array)):
        if new_array[idx] == new_array[idx - 1] + 1:  
            count += 1
        else:
            longest = max(longest, count)   
            count = 1   

    return max(longest, count)   
    


def find_min_max(array:list)->int:
    largest = float('-inf')
    smallest  = float('inf')
    for index in range(len(array)):
        if array[index] > largest:
            largest = array[index]
        if array[index] < smallest:
            smallest = array[index]
    return largest,smallest



# using two pointer
def reverse_an_array(array:list)->list:
    start = 0
    end = len(array)-1

    while start <= end:
        array[end], array[start] = array[start],array[end]
        start +=1
        end = end - 1
    return array

# FInd the single number
def find_single_number(array:list)->int:
    d = {}
    for ele in array:
        if ele in d:
            d[ele] += 1
        else:
            d[ele] = 1
    print(d)
    for key in d:
        if d[key] == 1:
            return key
    return -1 

# Using XOR

def find_single_number_1(array:list)->int:
    ans = 0
    for ele in array:
        ans = ans ^ ele
    return ans
 


# Brute force 
def sub_array_1(array: list):
    length_of_array = len(array)
    max_sum = float('-inf')
    
    for i in range(length_of_array):
        curr_sum = 0
        for j in range(i, length_of_array):
            curr_sum += array[j]
            max_sum = max(curr_sum, max_sum)
    #         print(f"Subarray: {array[i:j+1]}, Sum: {curr_sum}")

    
    # print("Maximum subarray sum:", max_sum)
    return max_sum


# using kadane's algo
def using_kadane_algo_sub_array_1(array:list):
    curr_sum = 0
    max_sum = float('-inf')

    for index in range(len(array)):
        curr_sum += array[index]
        max_sum = max(curr_sum,max_sum)
        if curr_sum < 0:
            curr_sum = 0
    return max_sum

# Brute force solution
def two_pair_sum(array:list,tar):
    lenght_of_array = len(array)
    l = []
    for i in range(lenght_of_array):
        for j in range(i+1,lenght_of_array):
            if array[i] + array[j] == tar:
                l.append(i)
                l.append(j)
    return l

             
# Optimal solution  on sorted array- Using two pointer appo
def two_pair_optimal_solution(array: list, target: int):
    start = 0
    end = len(array) - 1
    result = []

    while start < end:
        curr_sum = array[start] + array[end]
        
        if curr_sum > target:
            end -= 1
        elif curr_sum < target:
            start += 1
        else:
            result.append((start, end))  # Store as tuple of indices
            start += 1
            end -= 1  # move both pointers to avoid infinite loop

    return result


# Brute force solution
def majority_count_element(array:list)->int:
    for val in array:
        freq = 0
        for ele in array:
            if val == ele:
                freq += 1
        if freq > (len(array) // 2):
            return val
    return -1


# Stock buy and sell

def stock_buy_and_sell(array:list)->int:
    best_buy = array[0]
    max_profit = 0
    for ele in array:
        if ele > best_buy:
            max_profit = max(max_profit,ele-best_buy)
        best_buy = min(best_buy,ele)
    return max_profit





print("result=================>",stock_buy_and_sell([7,1,5,3,6,4]))




 
 

 
 


