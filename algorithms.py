
#binary search using iterative loop

# def binary_search(arr, x):
# 	low = 0
# 	high = len(arr) - 1
# 	mid = 0
#
# 	while low <= high:
#
# 		mid = (high + low) // 2
#
#
# 		if arr[mid] < x:    #if mid value is lesser, than low index value is (middle index + 1)
# 			low = mid + 1
#
#
# 		elif arr[mid] > x:  #if mid value is greater, than high index value is (middle index - 1)
# 			high = mid - 1
#
#
# 		else:    #this case will return the searched index finally
# 			return mid
#
#
# 	return -1  # If we reach here, then the element was not present
#
# # Test array
# arr = [ 2, 3, 4, 10, 40, 70,75,80,85,90]
# x = 85
#
# result = binary_search(arr, x)
#
# if result != -1:
# 	print("Element is present at index", str(result))
# else:
# 	print("Element is not present in array")



#binary search using recursion


# def binary_search(arr,low,high, x):
#
#     if high>=low:
#
#         mid = (high + low) // 2
#
#
#         if arr[mid] < x:    #if mid value is lesser, than low index value is (middle index + 1)
#             return binary_search(arr,mid+1,high,x)
#
#         elif arr[mid] > x:  #if mid value is greater, than high index value is (middle index - 1)
#             return binary_search(arr,low,mid-1,x)
#
#
#         else:    #this case will return the searched index finally
#             return mid
#
#     else:
# 	    return -1  # If we reach here, then the element was not present
#
#
# arr = [ 2, 3, 4, 10, 40,60, 78, 89 ]
# x = 78
# low = 0
# high = len(arr) - 1
# result = binary_search(arr,low,high, x)
#
# if result != -1:
# 	print("Element is present at index", str(result))
# else:
# 	print("Element is not present in array")

#binary search time complexity - worst case - O(log(n)  # Best case- O(1), If mid value is the searching value,

#binary search space complexity - Iterative method - O(1), Recursive method - O(log n)





# # Counting sort in Python programming
#
# # https://www.programiz.com/dsa/counting-sort   #refered this
#
# #counting sort - Places the input array values into output array values based on the indexes.
# # In between input and output array, we created and uses count array upto the maximum input element
#
# #Time complexity worst case = O(N+K)  -- K is maximum input number

#It will be more faster on sorting string characters, because it maximum 26+26 upper&lower characters only
#
# def countingSort(array):
#     size = len(array)
#     output = [0] * size
#     max_input_value=(max(array)+1)
#     count = [0] * max_input_value   #have to create upto the length of maximum input element
#
#
#     for i in range(0, size):
#         count[array[i]] += 1   #count list = occurences of input elements from input array
#
#     # Store the cummulative count
#     for i in range(1, max_input_value):
#         count[i] = count[i] + count[i - 1]   #count list = sum of current and previous index values
#
#
#
#     for i in range(size):
#         output_index = count[array[i]] - 1    #Finds the output index - count[array[i]] == input array value is index of count array value,  then minus 1
#         output[output_index] = array[i]     #places the input array elements into ouput array indexes
#         count[array[i]] = count[array[i]] - 1  #this case - handles duplicates of input elements
#
#     print("output_array",output)
#
#     for i in range(0, size):  # Copy the sorted output elements into original array
#         array[i] = output[i]
#
#
# data = [4, 2, 2, 8, 3, 3, 1]
# countingSort(data)
# print("Sorted Array in Ascending Order: ")
# print(data)    #[1, 2, 2, 3, 3, 4, 8]



# selection sorting - On every 'i'th for loop iteration, Compares and places the possible minimum value from 0th index to end index.

# arr = [13, 4, 9, 5, 3, 16, 12]
# for i in range(len(arr)):
#     minimum = i  # assumes 'i' index is minimum
#
#     for j in range(i + 1, len(arr)):
#         if arr[j] < arr[minimum]:
#             minimum = j  # After completed 'j' for loop, gets the minimum value (if not found - "minimum = i" still maintains)
#
#     arr[i], arr[minimum] = arr[minimum], arr[i]  # swaps the above found minimum value with arr[i],
#
# print(arr)



#Insertion Sorting program -
#
# # Similar to inserting a value in some index, so iterating from last index.
#
# # https://www.tutorialspoint.com/insertion-sort-in-python-program
#
# # Ex: i = 4, j will iterate from 3 to 0, if j values lesser than key value ex: arr[i], will insert the key value
#
#
# arr = [13, 4, 9, 5, 3, 16, 12]
#
# for i in range(1,len(arr)):
#     key = arr[i]
#     j = i - 1
#
#     while j>=0 and key < arr[j]:
#         arr[j+1] = arr[j]   #inserting will duplicate the values Ex: [0,3,2],i=2, key = arr[i] == 2 , j = i-1 -- j=1,  -- arr[j+1] = arr[j] -- [0,3,3]
#         j = j - 1   #minimize j value into 1 (while loop j condition)
#
#     arr[j+1] = key #Once while loop ended, placing the key value from the above insertion, "j = 1" after j = j - 1, [0,2,3]
#     # (If no minimum value from while loop, placing key value in same 'i' index, which means no changes in that 'i' iteration)
#
#     print(i,j,key,arr)
#
# print(arr)




# #Python program for implementation of Quicksort
#
# #Quick sort General logic - Selects the pivot, right side elements should be lesser than pivot.
# # Left side elements should be greater than pivot.
# #uses recursion seperatly, to sort the right side elements and left side elements. (from pivot)
#
#
# #below quick sort program logic:
# #Note - Below program, always takes last element as pivot.
# #Increasing index starts from (0 - high) and increases (1 - high), .. (4-high) (because 0,1,2,3 indexes already sorted in previous recursive calls)
#
#
def pivot_control_main_swapping(arr,low,high):
    i = low - 1
    pivot = arr[high]   #always takes last element as pivot.

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            if i != j:
                arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]  #After the for loop, swapping the pivot value(arr[high]) with i+1, because before i+1 indexes are smaller than pivot from above for loop.
    # In the end, pivot value also changes for next function call.

    return (i+1)

def quick_sort_intermediate_function(arr,low,high):

    if len(arr) <= 1:
        return arr

    if low < high:

        increasing_index = pivot_control_main_swapping(arr,low,high)  #increasing_index increases Ex: 0 to high, 1 to high, 4 to high(because 0,1,2,3 already sorted) etc
        print('Index', increasing_index)
        quick_sort_intermediate_function(arr,low,increasing_index-1)  #Ex: Again sorts - From 0th index to increasing_index-1

        quick_sort_intermediate_function(arr,increasing_index+1,high)  #Again sorts - increasing_index+1 to len(elements)-1

        return arr


arr = [2,0,3,6,5,4,1]
arr = [10, 7, 8, 9, 1, 5]
print(quick_sort_intermediate_function(arr,0,len(arr)-1))




#Mergesort python program

#Merge sort logic - splits, sorts and merge(inserts into main 'arr' by index)


# Ex: [2,0,3,5,4,1] - splitting and sorting
# [2,0,3], [5,4,1] - input splitted as two halfs
#
# 1) [2,0,3]
# [2],[0,3] - After sorting then inserts into 'arr' list - [0,3] - [0,3]
# -- [2,0,3] - After sorting then inserts into 'arr' list - [2,0,3] - [0,2,3]
#
# 2) [5,4,1]
# [5],[4,1] - After sorting then inserts into 'arr' list - [4,1] - [1,4]
# -- [5,1,4] - After sorting then inserts into 'arr' list - [5,1,4] - [1,4,5]

#final sorting - left - [0,2,3] , right - [1,4,5], then inserts into 'arr' list - [2,0,3,5,4,1] - [0,1,2,3,4,5]

#so finally output - [0,1,2,3,4,5]


# def merge_sort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         left = arr[:mid]
#         right = arr[mid:]
#
#         merge_sort(left)
#         merge_sort(right)
#
#         i = 0    #left side splitted list
#         j = 0    #right side splitted list
#         k = 0    #main list 'arr'
#
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:   #if left splitted list value is lesser than right list, inserts value in main 'arr' list
#                 arr[k] = left[i]
#                 i = i + 1
#             else:
#                 arr[k] = right[j]  #else condition - inserts right list values
#                 j = j+1
#             k = k + 1      #increments k value for every iteration
#
# #From above while loop, either i (left) inserts all values (or) j (right) inserts all values in main 'arr' list
#
#         while i < len(left):   #remaining i (left) values inserts in main 'arr' list
#             arr[k] = left[i]
#             i = i + 1
#             k = k + 1
#
#         while j < len(right):   #remaining i (right) values inserts in main 'arr' list
#             arr[k] = right[j]
#             j = j + 1
#             k = k + 1
#
#
# arr = [2,0,3,5,4,1]
# merge_sort(arr)
# print(arr)

#Merge sort Time complexity - Splits the list into half(divide and conquer) using recursion - O(log(n)),
# Then remaining while loops O(n), So totally O(n*logn)





#O(n) optimized/modified bubble sort algorithm- Best case (For already sorted input elements)
#
# # Normal Bubble sort - always runs for O(n^2) for all cases
#
# def bubbleSort(arr):
#     n = len(arr)
#
#     for i in range(n):
#         swapped = False
#
#         for j in range(i + 1, len(arr)):
#             if arr[i] > arr[j]:   #Ex: [0,1,2,3,4] , i=0, j=i+1 == 1, checks 0>1,0>2,0>3,0>4,
#                 # So No swaps after checked with entire adjacent elements, SO it means already the input list is sorted.
#                 #still swapped = False, below it breaks the loop.
#                 arr[i], arr[j] = arr[j], arr[i]
#                 swapped = True
#
#         if swapped == False:   #so here we breaks the parent for loop and ends iteration.
#             break
#
# arr = [4,5,6,0,1]
# arr = [0,1,2,3,4]
#
# bubbleSort(arr)
#
# print("Sorted array :",arr)