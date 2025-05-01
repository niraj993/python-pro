def binary_search_also(array:list,target:int)->int:
    low,high = 0,len(array)-1

    while low <= high:
        mid = (low+high)//2
        if array[mid] == target:
            return mid
        elif target > array[mid]:
            low = mid + 1
        else:
            high = mid-1
    return -1


def binary_search_low_bound(array:list,target:int)->int:
    low,high = 0,len(array)-1
    awswer = len(array)
    while low <= high:
        mid = (low + high) // 2
        if array[mid] >= target:
            awswer = mid
            high = mid-1
        else:
            low = mid+1
    return awswer



def binary_search_upper_bound(array:list,target:int)->int:
    length = len(array)
    low,high = 0,length-1
    answer =length
    while low <= high:
        mid = (low+high)//2
        if array[mid] > answer:
            answer = mid
            high = mid - 1
        else:
            low = mid+1
    return answer
        


def search_insert(array: list, target: int) -> int:
    low, high = 0, len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid  # Found, return index
        elif array[mid] < target:
            low = mid + 1  # Move right
        else:
            high = mid - 1  # Move left

    # If not found, insert at the correct position and return index
    array.insert(low, target)
    return low  # `low` is the correct insert position



def ceil_and_floor_using_binary_search(array:list):
    lenght= len(array)
    low,high = 0,lenght-1
    answer = lenght
    while low <= high:
        mid = (low+high)//2
        if array[mid] <= mid:
            answer = array[mid]
            low = mid + 1
        else:
            high = mid-1
    return answer



# Find first and last occurence an array in sorted array
# Brute force solution using leniar search

def find_first_and_last_occu(array:list,elemenet:int)->int:
    lenght = len(array)
    first = -1
    last = -1
    for idx in range(0,lenght):
        if array[idx] == elemenet:
            if first == -1:
                first = idx
            last = idx
    return first,last

# Using Binary serach
def find_first_and_last_occurence_1(array:list,element:int)->int:
    low,high = 0,len(array)-1
    first = -1
    last = -1
    while low <= high:
        mid = (low + high)//2
        if array[mid] == element:
            first = mid
            high = mid -1
        elif array[mid] < element:
            low = mid + 1
        else:
            high = mid-1
    
    low, high = 0, len(array) - 1  
    while low<=high:
        mid = (low+high)//2
        if array[mid] == element:
            last = mid
            low = mid+1
        elif array[mid] < element:
            low = mid+1
        else:
            high = mid-1

    return first,last
    


print("result is ===========>",find_first_and_last_occurence_1(array=[1,2,3,4,5,5,6,7],element=5))
