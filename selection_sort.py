

def selection_sort(array:list)->list:
    
    for i in range(len(array)-1):
        mini = i
        for j in range(i + 1,len(array)):
            if array[j] < array[mini]:
                mini = j
        array[i],array[mini] = array[mini],array[i]
    return array

arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print(sorted_arr)  # Output: [11, 12, 22, 25, 64]