



# class A():
#     __s=10
#     def __init__(self,*args, **kwargs):
#         print(args, kwargs)
#
# # s=A(359,3254,470426704,406,'fff',a=12,b=23)
# d=A('444')
# # print(d._A.__s)
#
# class AAA(Exception):
#     def __init__(self,error_message):
#         self.error=error_message
#
#     def __str__(self):
#         return self.error

# try:
#     a=12
#     d=2/0
# except Exception as err:
#     raise (err)
#     print('gggg')





# def f2():
#     s=2/0      #this exception is raised from below function code
#     return 'gtgt'
#
#
# def f1():
#     try:
#         print('ggg')
#         return f2()
#     except Exception as err:
#         print('HHHHH')
#         raise (err)    #if i didn't raised exception, above 's=2/0' inside f2(), Exception will be passed.
#
# print(f1())


#for -loop factorial

# def loop_for(n):
#     if n<1:
#         return
#     for i in range(2):
#         print(n)
#         for j in range(2):
#             print(j,n)
#         loop_for(n-1)
#
# loop_for(5)



# s='sathish'
# d=[]
# # d=[i for i in s if i not in d elif i in d d.remove(i)]
# d.append(i if i not in d else d.remove(i) for i in s)
# # print(str(i) for i in list(d))
# print(list(d))


# s='1123'

# def subs(string, ret=['']):
#     if len(string) == 0:
#         return ret
#     head, tail = string[0], string[1:]
#     ret = ret + list(map(lambda x: x+head, ret))
#     return subs(tail, ret)
#
# print(subs('abc'))



# def return_substrings(s):
#     all_sub = set()
#     recent = {s}
#     print(recent)
#
#     while recent:
#         tmp = set()
#         for word in recent:
#             for i in range(len(word)):
#                 tmp.add(word[:i] + word[i + 1:])
#                 print('ttt',tmp)
#         all_sub.update(recent)
#         recent = tmp
#
#     return all_sub
#
#
# print(return_substrings('abcd'))







#program to print next big number using same digits (one test case, needs to add)
# def next_greatest_number(num):
#     if num==sorted(num,reverse=True):
#         return "Already it is a greatest number"
#     if num==sorted(num):
#         num[-1], num[-2] = num[-2], num[-1]
#         return num
#     check_string="".join(list(map(str,num)))
#     print(check_string)
#     last_index=num[len(num)-1]
#     for i in range(len(num)-2,0,-1):
#         if last_index>num[i]:
#             # num.insert(i,num[i])
#             print('ff',i)
#             # final_string=check_string[:i]+str(last_index)+check_string[i:]
#             # print(final_string,check_string[:i],str(last_index),check_string[i:])
#             # final_string=final_string[:len(num)]
#             # return(list(final_string))
#             # num[last_index],num[i] = num[i], num[last_index]
#             # return num
#             num.insert(i,last_index)
#             return num[:len(num)-1]
#
# num=[1,2,4,3]
# num=[2,1,8,7,6,5]
# print(next_greatest_number(num))






#all substring combinations using slicing (linear indexes Ex: 0:1, 0:2,1:2,1:3)
# test_str = "abcd"
# test_str='1123'
# test_str='213'
#
# # Using list comprehension + string slicing
# res = [test_str[i: j] for i in range(len(test_str))
#        for j in range(i + 1, len(test_str) + 1)]
#
#
#
#
# # printing result
# print("All substrings of string are : " + str(res))    #['a', 'ab', 'abc', 'abcd', 'b', 'bc', 'bcd', 'c', 'cd', 'd']




# def different_swapping(a,b,interval=None):
#     tmp1=a
#     tmp2=b
#     b="CBACCBBAC"
#     b=list(b)
#     a="BCCABCBCA"
#     # a='ABCDEF'
#     a=list(a)
#
#     c=0
#     if sorted(a)==sorted(b):
#         for i in range(len(a)):
#             for j in range(len(a)):
#                 if a[i] != a[j]:
#                     a[i],a[j]=a[j],a[i]
#                     print(a)
#                     c=c+1
#                     if a==b:
#                         # print("ggggg",a,b)
#                         return ("condition satisfied ---1: ", a,b)
#         print(c)
#     else:
#         return ("swapping not possible")
#
#     a="BCCABCBCA"
#     a=list(a)
#     for i in range(0,len(a)-1,2):
#         print(i,i+1)
#         a[i+1],a[i]=a[i],a[i+1]
#         print(a)

#
# def toString(List):
#     return ''.join(List)
# #
# #
# # # Function to print permutations of string
# # # This function takes three parameters:
# # # 1. String
# # # 2. Starting index of the string
# # # 3. Ending index of the string.
# def permute(a, l, r):
#     if l == r:
#         print (toString(a))
#     else:
#         for i in range(l, r + 1):
#             a[l], a[i] = a[i], a[l]
#             permute(a, l + 1, r)
#             a[l], a[i] = a[i], a[l]  # backtrack
#
#
# # Driver program to test the above function
# string = "ABCDE"
# n = len(string)
# a = list(string)
# permute(a, 0, n - 1)








# f=[3, 1, -2, -2, -1, 3]
# flag=1
# checking_order="Decreasing" if f[0]>f[1] else "Increasing"
# i=1
# j=i+1
# # if checking_order=='Decreasing':
# while flag>-1:
#     try:
#         if checking_order=='Decreasing':
#             if not f[i]>f[j]:
#                 flag=flag-1
#                 checking_order='Increasing'
#
#         elif checking_order=='Increasing':
#             if not f[i] < f[j]:
#                 flag = flag - 1
#                 checking_order = 'Decreasing'
#
#         i = i + 1
#         j = j + 1
#
#     except Exception as err:
#         print (err)
#         continue
#
# print(i,j, checking_order)



















# DFS: iterative implement.

# def isValid(first, second, others):
#     if ((len(first) > 1 and first[0] == "0") or
#             (len(second) > 1 and second[0] == "0")):
#         return False
#     sum_str = str(int(first) + int(second))
#     if sum_str == others:
#         return True
#     elif others.startswith(sum_str):
#         return isValid(second, sum_str, others[len(sum_str):])
#     else:
#         return False
#
#
# def is_additive_number(num):
#     length = len(num)
#     for i in range(1, int(length/2+1)):
#         for j in range(1, int((length-i)/2 + 1)):
#             first, second, others = num[:i], num[i:i+j], num[i+j:]
#             if isValid(first, second, others):
#                 return True
#     return False
#
#
# a=1
# print(is_additive_number('66121830'))
# print(is_additive_number('110101201'))







# s='66121830'
# i=0
# while i<len(s):
#     print(s[i])
#     i=i+1





# def inserting(s,pos):
#     for i in range(len(s)-2,pos,-1):
#         s[i+1]=s[i]
#         # print(s[i],s)
#     print(s)
#
# s=[10,20,30,40]
# s.append('@')
# print(inserting(s,2))
# # s[4]=99
# # print(s)


#prints missing numbers between two numbers in the list
# s=[2,4,6,8,9]
# i=0
# while i<len(s)-1:
#     for j in list((range(s[i]+1,s[i+1]))):   #creates range between two elements
#         print(j),     #3 5 7
#     i=i+1











# import itertools
# print (list(itertools.combinations('abcd',3)))
# from itertools import groupby
# for i,j in groupby('AAAAABBCCCCCDDDCCCBBA'):
# 	print (i,list(j))
# a=[[10,20],[30,40]]
# s=itertools.product(a)
# print(list(s))
# itertools.
#
# import collections
# collections.










# result=[]
# input_number=10
# for i in range(2,input_number+1):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         result.append(i)
# print(len(result))

# k=2
# input_list=[1,2,3,4,5]
# # input_list=[1,1,3,5,5]
# # input_list=[6,7,11,7,6,8]
# # input_list=[-7,22,17,3]
# median_value=(len(input_list)-1)//2
# # print(median_value,input_list[median_value])
# result=[]
# input_list=list(sorted(input_list))
# # print(input_list)
# for i in input_list:
#     val=abs(i-input_list[median_value])
#     result.append([i,val])
# # print(result)
#
# s=list(sorted(result,reverse=True,key=lambda x:x[1]))
# print(s)
#
# for i in range(len(s)-1):
#     for n in range(i+1,len(s)-1):
#         if s[i][1]==s[n][1]:
#             if s[i][0]<s[n][0]:
#                 s[i],s[n]=s[n],s[i]
# print(s)
#
# final_Result=[i for i,j in s]
# result_value=final_Result[:k]
# print(final_Result)
# print(result_value)



#removes particular letter using recursion and slicing
# def letter_removing_recursion(string,letter):
#     if len(string)==0:
#         return ""
#     if string[0]==letter:
#         return letter_removing_recursion(string[1:],letter)   #slicing the letters from 1st index
#     return string[0]+letter_removing_recursion(string[1:],letter)
#
#
# string="geeksforgeeks"
# string='sathish'   #athih
# s='s'
# print(letter_removing_recursion(string,s))



#
# test_list = ["Gfg", 3, "is", 8, "Best", 10, "for", 18, "Geeks", 33]
#
# key_list = ["name", "number"]
#
# input_list=[test_list[i:i+2] for i in range(0,len(test_list),2)]
#
# print(input_list)
#
# d={}
# for i in test_list:
#     for j in list(zip(i,key_list)):
#         d.update([j])
# print(d)







# def check_counts(a,b,c):
#     if a==b:
#         return 0
#     if a*c==b:
#         return 1
#     count=1
#     tmp1=0
#     if a*c>b:
#         tmp=a*c
#         if b!=tmp and b<tmp:
#             while 1:
#                 if tmp%2==0:
#                     tmp=tmp-2
#                     count=count+1
#                     # print("1",count)
#                 else:
#                     tmp=tmp-1
#                     count=count+1
#                     # print("2", count)
#                 if tmp<=b:
#                     break
#         return count
#
#
#     #
#     # if a*c<b:
#     #     tmp=a*c
#     #     while 1:
#     #         if tmp<b:
#     #             tmp=tmp+(a*c)
#     #         else:
#     #             break
#
#
# print(check_counts(3,5,2))



tables1=[10,20,30,40,50]
tables2=[10,30,50]








# def check_numbers(n,tmp,a):
#     if n==1:
#         return 1
#     else:
#         c=(a + tmp)
#         print(c)
#         a=tmp
#         tmp=tmp+1
#         return check_numbers(n-1,tmp,a)
#
#
# n=5
# tmp=1
# a=0
# print(check_numbers(n,tmp,a))

















# a=0
# tmp=1
# for i in range(5+1):
#     print(a+tmp)
#     a=i+tmp
#     print('tmp',a,tmp)
#     tmp=tmp+1






# n=4
# g=1
# for i in range(n):
#     for j in range(n,i-0,-1):
#         print(j,end=" ")
#     if i>1:
#         print('*'*g,end=" ")
#     for k in range(2+i,n+1):
#         print(k,end=" ")
#     print("\n")
#     g=g+2

#


# n=4
# tmp=[i for i in range(1,n+1)]
# # print(tmp)
# for i in range(0,n):
#     s=(tmp[n-1:i:-1])










# def QuickSort(arr):
#     elements = len(arr)
#
#     # Base case
#     if elements < 2:
#         return arr
#
#     current_position = 0  # Position of the partitioning element
#
#     for i in range(1, elements):  # Partitioning loop
#         if arr[i] <= arr[0]:
#             current_position += 1
#             temp = arr[i]
#             arr[i] = arr[current_position]
#             arr[current_position] = temp
#     print('gggg',arr)
#
#     temp = arr[0]
#     arr[0] = arr[current_position]
#     arr[current_position] = temp  # Brings pivot to it's appropriate position
#
#     left = QuickSort(arr[0:current_position])  # Sorts the elements to the left of pivot
#     right = QuickSort(arr[current_position + 1:elements])  # sorts the elements to the right of pivot
#     arr = left + [arr[current_position]] + right  # Merging everything together
#     print('left',left)
#     print('current position',[arr[current_position]])
#     print('right', right)
#     print('final_array',arr)
#
#     return arr
#
#
# array_to_be_sorted = [4, 2, 0, 3, 1, 5]
# print("Original Array: ", array_to_be_sorted)
# print("Sorted Array: ", QuickSort(array_to_be_sorted))













#




# prev_list=['BC']
# str='A'
# a = prev_list[0][0:2]
# # b = str
# # c = prev_list[i][j:len(str) - 1]
# print(a)



# def permute_string(str):
#     if len(str) == 0:
#         return ['']
#     prev_list = permute_string(str[1:len(str)])
#     next_list = []
#     for i in range(0,len(prev_list)):
#         for j in range(0,len(str)):
#             a=prev_list[i][0:j]
#             b=str[0]
#             c=prev_list[i][j:len(str)-1]
#             new_str = a + b + c
#             print('a= ',a,'b= ',b,'c= ',c,'----',new_str)
#             if new_str not in next_list:
#                 next_list.append(new_str)
#     return next_list
#
# print(permute_string('ABC'));



#regex using the (find and replace with count=3,)
import re
input_string="satatatatatata"
# matching_string=r'a'
# replacing_string="@"
#
# output=re.sub(matching_string,replacing_string,input_string,count=3,flags=re.I)  #ignores the upper/lower case difference in matching
# print(output)    #s@t@t@tatatat  #find and replaced only first three "(count=3)" occurences
#

# #Regex for Ipv4
# ^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$
#
# #
# #find and replace the string with the range(using regex finditer())
# import re
# input_string = "satatatatatata"
# matching_string = "a"
# replacing_string = "@"
# starting_range = 5
# end_range=10
# indexes=re.finditer(matching_string,input_string)
# result_string=list(input_string)
# for i in indexes:
#     index=(i.start())
#     if (index >= starting_range) and (index <= end_range):
#         result_string[index] = replacing_string
# print("input_string - ", input_string)
# print("output_string after replaced within the range - ","".join(result_string))





#
# def ff():
# 	f=10
# 	print(id(f))
#
# ff()
#
#
# a=10
# d=[20,10,30]
# print(id(a),id(d[1]),id(d))
#
# s=(1,2,3)
# s1=(1,2,3)
# print(id(s),id(s1))
# s=s+()
# print(id(s))
#
# s=[1,2,3]
# s1=[1,2,3]
# print(id(s),id(s1))
# s=s+s1
# print(id(s))



# 
# def test():
# 	pass
# 
# def test(a=None):
# 	print('hello')
# 
# test()

# import re
# input_string = """Python has the same structure as Perl, but, unlike Perl, includes it in the syntax of the language. The order of inheritance affects the class semantics. Python had to deal with this upon the introduction of new-style classes, all of which have a common ancestor, object. Python creates a list of classes using the C3 linearization (or Method Resolution Order (MRO)) algorithm"""
# matching_string = "the"
# replacing_string = "@"
# starting_range = 10      #starting range should be less than length of inout string
# end_range = 500
# left_side = input_string[:starting_range]
# right_side = input_string[end_range+1:]
# executing_string = input_string[starting_range:end_range+1]  #slices the string from starting and end range
# print(left_side,"---",right_side,"---",executing_string)
# if matching_string in executing_string:
# 	tmp = re.sub(matching_string,replacing_string,executing_string,flags=re.MULTILINE)
# 	final_string = left_side + tmp + right_side
# 	print("Replaced string within the {} to {} range---".format(starting_range,end_range),final_string)
# else:
# 	print('!!!Matching string is not present in the given input string or within input range')


# import re
#
# def find_replace_range(input_string,matching_string,replacing_string,starting_range=0,end_range=len(input_string)):
#     if starting_range >= len(input_string):
#         return "starting range should be less than length of input string"
#     left_side = input_string[:starting_range]
#     right_side = input_string[end_range + 1:]
#     executing_string = input_string[starting_range:end_range + 1]  # slices the string from starting and end range
#     print(left_side, "---", right_side, "---", executing_string)
#     if matching_string in executing_string:
#         tmp = re.sub(matching_string, replacing_string, executing_string, flags=re.MULTILINE)    #replacing using re.sub()
#         final_string = left_side + tmp + right_side
#         return "Replaced string within the {} to {} range---".format(starting_range, end_range), final_string
#     else:
#         return ('!!!Matching string is not present in the given input string or within input range')
#
#
# input_string = """Python has the same structure as the Perl, but, unlike the Perl, includes it in the syntax of the language. With this upon the introduction"""
# matching_string = "the"
# replacing_string = "@"
# starting_range = 10      #starting range should be less than length of inout string
# end_range = 30
# input_string = input_string.split()
# print(find_replace_range(input_string,matching_string,replacing_string,starting_range,end_range))



# class A:
#     # def __init__(self):
#     #     print('class A init')
#     def do_thing(self):
#         print('class A method')
#
#
#
# class B(A):
#     # def __init__(self):
#     #     print('class B init')
#     #     super().__init__()
#     def do_thing(self):
#         print('class B method')
#         super().do_thing()
#
# class C(A):
#     # def __init__(self):
#     #     print('class C init')
#     #     super().__init__()
#     def do_thing(self):
#         print('class C method')
#         super().do_thing()
#
# class D(B, C):
#     # def __init__(self):
#     #     print('class D init')
#     #     super().__init__()
#     def do_thing(self):
#         print('Class D method')
#         super().do_thing()
#
# d = D()
# d.do_thing()
# print(D.__mro__)
# # d.do_thing()






# #Diamond Problem - Python internally solves the diamond problem and multiple inheritance using the super() and method resolution order mro(), by executing the classes from left to right side classes.
# #Super() - Internally follows the method resolution order normally. In Multiple inheritance, it executes all super classes from left to right side.
#
#
# class A:
#
#     def do_thing(self):
#         print('class A method')
#
#
# class B(A):
#
#     def do_thing(self):
#         print('class B method')
#         super().do_thing()
#
# class C(A):
#
#     def do_thing(self):
#         print('class C method')
#         super().do_thing()
#
# class D(B, C):
#
#     def do_thing(self):
#         print('Class D method')
#         super().do_thing()
#
# obj = D()
# print("Sub-class 'D' method resolution order - ", D.__mro__)
# obj.do_thing()




import re

# string='my name is sai sai '
#
# t= re.sub(r'\bsai\b', r'\1-suresh', string)
#
# # t= re.sub(r'^\b(\w+)\s+\1\b$', r'\1suresh', string)
#
# print (t)

#r'^\b(\w+)\s+\1\b$'  #

#(.+)(?=\1+)

# r=re.search(r'\b(the).*\1\b','the signature the the the thesaurs')
# print(r.group())
# print(r.groups(2))
# for i in (r.groups()): print (i)


#Find Repetitive and replaced the string using regex

# input_string = 'the earth is the the the third planet of the the the the solar system with the the sun.'
# repetitive_string = 'the'
# pattern=r'\b({})(?:\s+\1\b)+'.format(repetitive_string)   #passing matching input into regex
# output_string=re.sub(pattern,repetitive_string,input_string,flags=re.M)
# print("Input_string --- ",input_string)
# print("Repetitive replaced output string --- ",output_string)

# Input_string ---  the earth is the the the third planet of the the the the solar system with the the sun.
# Repetitive replaced output string ---  the earth is the third planet of the solar system with the sun.

# c=4
# n=16
# iteration=0
# for i in range(0,n,c):
#     iteration = iteration +1
#     c = c + 4
# print(iteration)
#
# iteration=0
# for i in range(1000):
#     for j in range(1000):
#         for k in range(250):
#             iteration = iteration + 1
# print(iteration)




# Python program for implementation of MergeSort
# def mergeSort(arr):
# 	if len(arr) > 1:
# 		mid = len(arr) // 2  # Finding the mid of the array
# 		L = arr[:mid]  # Dividing the array elements
# 		R = arr[mid:]  # into 2 halves
#
# 		mergeSort(L)  # Sorting the first half
# 		mergeSort(R)  # Sorting the second half
#
# 		i = j = k = 0
#
# 		# Copy data to temp arrays L[] and R[]
# 		while i < len(L) and j < len(R):
# 			if L[i] < R[j]:
# 				arr[k] = L[i]
# 				i += 1
# 			else:
# 				arr[k] = R[j]
# 				j += 1
# 			k += 1
#
# 		# Checking if any element was left
# 		while i < len(L):
# 			arr[k] = L[i]
# 			i += 1
# 			k += 1
#
# 		while j < len(R):
# 			arr[k] = R[j]
# 			j += 1
# 			k += 1
#
#
#
#
# # driver code to test the above code
# if __name__ == '__main__':
# 	arr = [4,2,0,1,5,3]
# 	arr = [4, 2, 0]
# 	print("Given array is", arr)
# 	mergeSort(arr)
# 	print("Sorted array is: ",arr)




#
# def mergeSort(myList):
#     if len(myList) > 1:
#         mid = len(myList) // 2
#         left = myList[:mid]
#         right = myList[mid:]
#         mergeSort(left)
#         mergeSort(right)
#         # Two iterators for traversing the two halves
#         i = 0
#         j = 0
#         # Iterator for the main list
#         k = 0
#
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 # The value from the left half has been used
#                 myList[k] = left[i]
#                 i += 1
#             else:
#                 myList[k] = right[j]
#                 j += 1
#             k += 1
#         print('list-111111', myList)
#
#         # For all the remaining values
#         while i < len(left):
#             myList[k] = left[i]
#             i += 1
#             k += 1
#         print('list-222222', myList)
#
#         while j < len(right):
#             myList[k] = right[j]
#             j += 1
#             k += 1
#         print('list-333333', myList)
#
#
# myList = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# myList = [2,0,3,5,4,1]
# mergeSort(myList)
# print(myList)


















# def mergeSort(myList,message):
#     if len(myList) > 1:
#         mid = len(myList) // 2
#         left = myList[:mid]
#         right = myList[mid:]
#         print('list -- ', myList,'left - ',left, 'middle - ', mid, 'right - ',right,'message - ',message)
#
#         # Recursive call on each half
#         mergeSort(left,'left_side')
#         mergeSort(right,'right_side')
#
# arr=[0,1,2,3,4,5]
# mergeSort(arr,'main')




# #O(n) optimized/modified bubble sort algorithm- Best case (For already sorted input elements)
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

#
# for i in range(len(arr)):
#     for j in range(i + 1, len(arr)):
#         if arr[i] > arr[j]:
#             arr[i], arr[j] = arr[j], arr[i]
#
# print("Sorted array :",arr)





















