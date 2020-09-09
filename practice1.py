

#sorting the sum of values
# list_one = [(122,4), (4,6,20), (10,2), (18,6,7,8,4)]
# print (sorted(list_one,key=lambda x: sum(x)))



# a=[1,2,3]
# b=a
# b.append(4)
# print(a,b,id(a),id(b))
#
# c=20
# b=c
# e=20
# print (b,c,e,id(c),id(b),id(e))









#decreasing and increasing numbers
# s=[4, 3, 8, 5, 6, 3, 8]
# p=[]
# for i in range(int(len(s))-2):
#     if not s[i]>s[i+1] and s[i+1]<s[i+2]:
#         break
#     else:
#         p.append(s[i])
# print (p)




# class Person:
#     def __init__(self, personName, personAge):
#         self.name = personName
#         self.age = personAge
#
#     def __str__(self):
#         return self.name,self.age
#
#     def __repr__(self):
#         return self.name
#
# p = Person('Pankaj', 34)
#
# print(p.__str__())
# print(p.__repr__())


# class ErrorCheck:
#
#     def __init__(self, function):
#         print (function)
#         self.function = function
#
#     def __call__(self, *params):
#         print (params)
#         if any([isinstance(i, str) for i in params]):
#             raise TypeError("parameter cannot be a string !!")
#         else:
#             return self.function(*params)


# def ErrorCheck(*params, **kwargs):
#     def inner(func):
#         print (params,kwargs)
#         if any([isinstance(i, str) for i in params]):
#             raise TypeError("parameter cannot be a string !!")
#         else:
#             return func()
#     return inner

# def ErrorCheck(*decor_params, **decor_kwargs):
#     print (decor_params, decor_kwargs)
#     def inner(func):
#         def wrap(*args,**kwargs):
#             print (args,kwargs)
#             if any([isinstance(i, str) for i in args]):
#                 raise TypeError("parameter cannot be a string !!")
#             else:
#                 return func(*args)
#         return wrap
#     return inner


# def ErrorCheck(func):
#     def inner():
#         print ("from inner function")
#         return func()
#     return inner

# def ErrorCheck(*params,**kwargs):
#     def inner(func):
#         print (params)
#         if any([isinstance(i, str) for i in params]):
#             raise TypeError("parameter cannot be a string !!")
#         else:
#             return func()
#     return inner

# def normal_function(*params):
#     print ("inside normal function")

# @ErrorCheck
# def normal_function(*params):
#     print("inside normal function")
#     for ele in params:
#         print(1,ele)
#
# # (ErrorCheck(normal_function)([1,2,3]))
# # (normal_function([1,2,3]))
# # print (ErrorCheck(normal_function)())
# (ErrorCheck([1,2,3],like="Hello")(normal_function)([12,34,5,6,7,8],hi=123))



# def ErrorCheck(func):
#     def inner(*params):
#         if any([isinstance(i, str) for i in params]):
#             raise TypeError("parameter cannot be a string !!")
#         else:
#             return func(*params)
#     return inner


# @ErrorCheck
# def add_numbers(*numbers):
#     return sum(numbers)


#  returns 6
# print (add_numbers(1,2,3))

# class Alphabet:
#     def __init__(self, value):
#         self.__value = value
#         self.__q=2000
#
#     # getting the values
#     # @property
#     def value(self):
#         print('Getting value')
#         return self.__value
#
#     def __pri_function(self):
#         print ('HEEELLLLOOO')
#     # setting the values
#     # @value.setter
#     def s_value(self, value):
#         print('Setting value to ' + value)
#         self.__value = value
#
#     # deleting the values
#     # @value.deleter
#     def d_value(self):
#         print('Deleting value')
#         del self.__value
#
#
# x = Alphabet('Peter')
# print (x._Alphabet__q)
# print (x._Alphabet__pri_function())
# print(x.value())  # ()  - No function braces should use to call property function.
#
# x.s_value('Diesel')
#
# # Modifying the “x.value”, will call automatically @value.setter. But inside that @value.setter function, code should modify the value.
#
# x.d_value()  # Deleting the “x.value”,  will call automatically @value.deleter.


# class Base:
#     def __init__(self):
#         self.__m='sat'
#         self.b=23
#         self._a = 2    # Protected variable
#
#     def _protected_function(self):    #protected function
#         print ("From protected function")
#
#
# class Derived(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print("Calling protected member of base class: ")
#         print(self._a)
#         print(self._protected_function())
#         # self._a=34
#         # print (self._a)
#
#
# obj1 = Derived()
#
# obj2 = Base()
#
# print(obj1._protected_function())
# print (obj1._a)
# print (obj2.b)
# print(obj2._a)
# obj2._a=364
# print(obj2._a)

# class DataCamp():
#     pass
#
#
# DataCampClass = type('DataCamp1',(),{})
# print(DataCampClass)
# print(DataCamp)
# print(DataCamp())
# print
#


# class MyMeta(type):
#     pass
#
# class MyClass(metaclass=MyMeta):
#     pass
#
# class MySubclass(MyClass):
#     pass
#
# print(type(MyMeta))
# print(type(MyClass))
# print(type(MySubclass))
#
# class A:pass
#
# print (type('sat'))
# print (type(str))
# print (type(dict))
# print (type(type))
# print (type(A))
#
#
# def fffp():
#     pass
#
# print (type(fffp))
#
#
# def test_method(self):
#     print("This is Test class method!")
#
# PythonClass = type('PythonClass', (), dict(start_date='August 2018',my_method=test_method))
# print(PythonClass)



# class DateTime(object):
#
#     def __init__(self, day=10, month=10, year=2000):
#         self.day = day
#         self.month = month
#         self.year = year
#         print (((day,month,year)))   #(20, 5, 1994)   #value get from below Classmethod and changes the class (DateTime) self.day,self.month,self.year values.
#     @classmethod
#     def from_string(cls, string_date):
#         day, month, year = map(int, string_date.split('-'))
#         myDate = cls(day, month, year)  #calling above Class Constructor and passing arguments.
#     @staticmethod
#     def is_valid_date(date_as_string):
#         day, month, year = map(int, date_as_string.split('-'))
#         return day <= 31 and month <= 12 and year <= 3999   #returns True
#
# DateTime.from_string('20-05-1994')   #calling Classmethod
# is_valid_date = DateTime.is_valid_date('20-05-1994')   #calling Staticmethod
# print(is_valid_date)  #prints True (from Staticmethod)

# class A:
#     def __init__(self,value=None):
#         self.value=value
#         # self.print_value()
#
#
#     def print_value(self):
#         print (self.value)
#
#     @classmethod
#     def getting_value(cls,value):
#         cls(value=value)
#
# s='ssss'
# # A.getting_value(s)
# obj=A(s)
# (obj.print_value())


# class py_solution:
#     def reverse_words(self,s):
#         return ' '.join(reversed(s.split()))
#
#
# print(py_solution().reverse_words('hello .py'))



# class A:
#     def __init__(self):
#         print ('A class')
#         self.test1='sathish'
#
#
# class B(A):
#     def __init__(self):
#         print('B class')
#         self.test = 'sathish'
#         super().__init__()
#
#
# obj=B()
# print (obj.test1)


# class Outer:
#     """Outer Class"""
#
#     def __init__(self):
#         print('Outer class constructor')
#         self.private = 'sample_private'
#         self.hello='Today'
#         self.inner = self.Inner()   ## instantiating the 'Inner' class
#
#
#     def reveal(self):
#         ## calling the 'Inner' class function display
#         self.inner.inner_display("Calling Inner class function from Outer class")
#
#     class Inner:
#         """Inner Class"""
#         def __init__(self,):
#             print('inner class constructor')
#
#         def inner_display(self, msg):
#             print(msg)
#
#
#
#
#
# obj=Outer()
# obj.reveal()
# (obj.Inner().inner_display('HIIIIIIIII'))
# (Outer.Inner().inner_display('HELLLLO'))

# ob=Outer.Inner()


# class A:
#     s='sat'
#
#     @staticmethod
#     def static_fun(a):
#         print (a,'heelo')
# ob=A()
# print (A.s)
# print (ob.s)
# (A.static_fun(10))


# class A:
#     pass
#
# class B(A):
#     pass
#
# print (B.A)

# print (20 + 6 * 2 ** 2 / 8 - 10)
#
# class Person:
#     def __init__(self, personName, personAge):
#         self.name = personName
#         self.age = personAge
#
#     def __str__(self):
#         return self.name
#
#     def __repr__(self):
#         return (self.name)
#
# p = Person('Pankaj', 34)
#
# print (Person)
# print (str(p))
# print (repr(p))
#
# name='sat'
# value= 23
# print (f"{name} has value for {value}")


#change tupe into dict

# def change_dict():
#     if len(test_list)==1:
#         return (dict(test_list))
#     else:
#         d={}
#         for i,j in test_list:
#             print (i,j)
#             if i in d:
#                 d[i]=d[i]+j
#             else:
#                 d[i]=j
#         return d
#
# test_list = [(5, 8)]
# print (change_dict())


# test_list = [(5), (5), (5), (5)],
# K = 5
#
# # Check if tuple list has all K
# # Using loop
# res = True
# for tup in test_list:
#     print (tup)
#     for ele in tup:
#         if ele != K:
#             res = False
#
# # printing result
# print("Are all elements K ? : " + str(res))


#logic to compare one by one item with other item  ex: sorting(bubble), sums of two values etc
# test_list = [1, 9, 5, 5, 7]
# test_list=[64, 34, 25, 12, 22, 11, 90]
# n = len(test_list)
# k = 10
# t=[]
# for i in range(len(test_list)):
#     for j in range(i+1,len(test_list)):
#         # if test_list[i]+test_list[j]==k:
#         #     s=(test_list[i],test_list[j])
#         #     t.append(s)
#         if test_list[i]>test_list[j]:
#             test_list[i],test_list[j]=test_list[j],test_list[i]
#
# print ((test_list))


# def sorting_method(list_one,reverse=False):
#     if not reverse:
#         for i in range(len(list_one)):
#             for j in range(i+1,len(list_one)):
#                 if sum(list_one[i]) > sum(list_one[j]):
#                     list_one[i],list_one[j]= list_one[j],list_one[i]
#     else:
#         for i in range(len(list_one)):
#             for j in range(i + 1, len(list_one)):
#                 if (sum(list_one[i]) < sum(list_one[j])):
#                     list_one[i], list_one[j] = list_one[j], list_one[i]
#     return list_one
#
# list_one = [(122,4), (4,6), (100,2), (18,4)]
# print(sorting_method(list_one))
# print(sorting_method(list_one,reverse=True))


# test_dict = {1 : 'Gfg is best for geeks', 2 : 'Gfg is good', 3 : 'I love Gfg'}
#
# sub_list = ['love', 'good']
# d={}
# for i,j in test_dict.items():
#     for k in j.split():
#         if k in sub_list:
#             break
#     else:
#         d.update([(i,j)])
#
# print (test_dict)
# print(d)


#finds the K value range

# test_list = [(0, 10), (11, 20), (21, 30), (31, 40)]
# K = 17
# f=[]
# for i,j in enumerate(test_list):
#     if j[0]<K and j[1]>K:
#         print (i)
#         break



# test_list = [('Gfg', 'best', 'geeks'), ('Gfg', 'good'),
#              ('Gfg', 'best', 'CS'), ('Gfg', 'love')]
#
# # printing original list
# print("The original list is : " + str(test_list))
#
# # initializing prefix tuple
# pref_tup = ('Gfg', 'best')
#
# p=[]
#
# for j in test_list:
#     tmp = (list(zip(j,pref_tup)))
#     print (tmp[0],tmp[1])
#     if tmp[0][0]==tmp[0][1] and tmp[1][0]==tmp[1][1]:
#         p.append(j)
# print (p)

#prime number


# for i in range(2,100):
#     for j in range(2,int(i)):
#         if i%j==0:
#             break
#     else:
#         print (i)


#palindrome
# d='mmadamm'
# c=0
# for i in range(int(len(d)/2)):
#     if d[i]!=d[len(d)-i-1]:
#         c=1
#         break
# print (c)

#deleting individual vaues greater than 10
# s=[[4, 5, 7],[5, 16, 8],[10, 7, 4]]
# for i in range(len(s)):
#     for j,k in enumerate(s[i]):
#         print(j,k)
#         if k>=10:
#             s[i].pop(j)   #removes using indexes
# print (s)


# d=[1,2,3,4]
# for i in range(0,4):
#     for j in range(0,4):
#         for k in range(0,4):
#             for l in range(0,4):
#                 if(i!=j&j!=k&k!=l&l!=i):
#                     print(d[i],d[j],d[k],d[l])



# test_dict = {"Gfg" : {'is' : 45, 'good' : 15},
#              'best' : {'for' : {'geeks' :  {'CS' : 12}}}}
#
# # printing original dictionary
# print("The original dictionary : " + str(test_dict))
#
# # initializing unwanted keys
# unw_keys = ['is', 'geeks']
#
# # del test_dict['Gfg']['is']
#
# print("The original dictionary : " + str(test_dict))
#
# print (test_dict.items())
#
# for i,j in test_dict.items():


#change nested dictionary into normal dictionary


# def insertion_sort(InputList):
#     for i in range(1, len(InputList)):
#         j = i - 1
#         nxt_element = InputList[i]
#         # Compare the current element with next one
#
#         while (InputList[j] > nxt_element) and (j >= 0):
#             InputList[j + 1] = InputList[j]
#             j = j - 1
#         InputList[j + 1] = nxt_element
#
#
# list = [19, 2, 31, 45, 30, 11, 121, 27]
# insertion_sort(list)
# print(list)


#stores only the non-repeated letters in each word
# t = 'geekforgeeks is best for geeks'
# test_str=t.split()
# k=[]
# for i in test_str:
#     tmp=[]
#     for j in i:
#         if (i.count(j)==1) and (j not in tmp):
#             tmp.append(j)
#     k.append(tmp)
# print (k)


# test_dict = {'Manjeet' : [1, 4, 5, 6],
#             'Akash' : [1, 8, 9],
#             'Nikhil': [10, 22, 4],
#             'Akshat': [5, 11, 22]}
#
#
# print (test_dict.values())
#
# for i,j,k in enumerate(test_dict.items()):
#     for p in k:
#         if p in


# def bsearch(list, val):
#
#     list_size = len(list) - 1
#
#     idx0 = 0
#     idxn = list_size
# # Find the middle most value
#
#     while idx0 <= idxn:
#         midval = (idx0 + idxn)// 2
#         print(idx0, idxn, midval)
#
#         if list[midval] == val:
#             return midval
# # Compare the value the middle most value
#         elif val > list[midval]:
#             idx0 = midval + 1
#         else:
#             idxn = midval - 1
#     return None
# # Initialize the sorted list
# list = [2,7,19,34,53,72]
#
# # Print the search result
# print(bsearch(list,72))
# print(bsearch(list,7))
#
#
#
# # Python 3 program for recursive binary search.
# # Modifications needed for the older Python 2 are found in comments.
#
# # Returns index of x in arr if present, else -1
# def binary_search(arr, low, high, x):
#
# 	# Check base case
# 	if high >= low:
#
# 		mid = (high + low) // 2
#
# 		# If element is present at the middle itself
# 		if arr[mid] == x:
# 			return mid
#
# 		# If element is smaller than mid, then it can only
# 		# be present in left subarray
# 		elif arr[mid] > x:
# 			return binary_search(arr, low, mid - 1, x)
#
# 		# Else the element can only be present in right subarray
# 		else:
# 			return binary_search(arr, mid + 1, high, x)
#
# 	else:
# 		# Element is not present in the array
# 		return -1
#
# # Test array
# arr = [ 2, 3, 4, 10, 40 ]
# x = 10
#
# # Function call
# result = binary_search(arr, 0, len(arr)-1, x)
#
# if result != -1:
# 	print("Element is present at index", str(result))
# else:
# 	print("Element is not present in array")
#

# test_list1 = [("g", "f"), ("g", "is"), ("be", "st")]
# test_list2 = [("fg", "g"), ("gf", "best"), ("st", " gfg")]
# print ([i[k]+j[k] for k in range(2) for i,j in zip(test_list1,test_list2)])

# d={}
# test_str = "GeeksforGeeks"
# for i in test_str:
#     if i not in d:
#         d[i]=test_str.count(i)
# s=sorted(list(d.items()),key=lambda x:x[1])
# print (s[0][0])

# import requests
# from requests.auth import HTTPBasicAuth
# headers = {'Authorization': 'Token 5f1dad9cc927fd85a180ce815db4c0319ef82f47'}
# response = requests.get("http://127.0.0.1:8000/person/",headers=headers)
# print (response.history)
# data = response.json()
# for i,j in dict(data).items():
#     print (i,'-----',j)
# print (data['email'])
# files={'file': open("C:\\Users\\Administrator\\Downloads\\003.jpg",'rb')}
# r = requests.put("http://127.0.0.1:8000/person/7",data={'person_name': 'pppalai', 'description': 'Hi pppalai'},auth = HTTPBasicAuth('sathish', 'Comodo@123'))


# print(r)
#
# # print content of request
# print(r.elapsed,"--------",r.content)
# response = requests.get("http://127.0.0.1:8000/person/")
# data = response.json()
# for i,j in dict(data).items():
#     print (i,'-----',j)

# s=requests.options("http://127.0.0.1:8000/person/1")
# print (s.headers)
#
#
# s=requests.head("http://127.0.0.1:8000/person/1")
# print (type(s))


# a=0
# b=1
# print (a,b),
# e=range(5)
# list_com=[i+j for i,j in enumerate(e)]
# print (list_com)



# def function_fian(val):
#     if val<=0:
#         return None
#     else:
#         return val*function_fian(val-1)
#
#
# print (function_fian(5))

# test_list = [(1, 2, 3), (6, 7, 6), (1, 6, 8)]
# print ([sum(i)/len(test_list) for i in test_list])
#
# print (zip(*test_list))


# test_list = ['man', 'a', 'gEek', 'for', 'GEEK', 'FoR']
# tmp=[]
# for i in range(len(test_list)):
#     for j in range(i+1,len(test_list)):
#         if test_list[i].lower()==test_list[j].lower():
#             tmp.append([test_list[i],test_list[j]])
#
# print(tmp)

# test_list = [9, 4, 5, 8, 10, 14]
# index_list = [1, 3, 4]
# c=1
# for i in index_list:
#     c=c*test_list[i]
# print(c)

# 0th index on every number is divisible by 2
# test_list = [25, 6, 228829, 432]
# tmp=[]
# for i in range(len(test_list)):
#     a=(str(test_list[i])[0])    #getting 0th index on every number
#     if int(a)%2==0:
#         tmp.append(True)
#     else:
#         tmp.append(False)
# print(all(tmp))

# print (["True" if int((str(test_list[i])[0]))%2==0 else "false" for i in range(len(test_list))])   #using list comprehension for above same program


#insering even values in even index and odd values in odd index
# test_list = [25, 6, 2288292, 432, 72,4,8,90,2,3,5]
# tmp=[0]*15
# print (tmp)
# even=0
# odd=1
# for i in test_list:
#     if i%2==0:
#         tmp[even]=i
#         even=even+2
#     else:
#         tmp[odd]=i
#         odd=odd+2
# greater_number=odd if odd>even else even
# print (tmp[0:greater_number-1])
# print(tmp,even,odd)

# test_list = [25, 6, 2288292, 432, 72,4,8,90,2,3,5]
# while 4 in test_list:
#     (test_list.remove(4))
#     print(test_list)

# s= "aabdbbtr"
# f=['e','a','r','t']
# d=set(s)
# t=(d.difference(set(f)))
# p=list(s)
# for i in t:
#     while i in p:
#         p.remove(i)
# print(p)


# def calc_factorial(x):
#     if x == 1:
#         return 1
#     else:
#         print (x)
#         return (x + calc_factorial(x-1))
#
# print (calc_factorial(5))


#recusion to count digits -- Inside recursion fun, should define return separetly in both if and else statements.

# def fff(d):
#     global c
#     if d>1:
#         c=c+1
#         fff((d/10))
#         return c
#     else:
# 	    return "Invalid input"
#
#
# d=23
# c=0
# print (fff((d)))



# def fian(d):
#     if d<=1:
#         return 0
#     else:
#         # for i in range(5):
#         return (fian(d-1)+fian(d-2))
#
#
# print (fian(5))


# def Fibonacci(n):
#     if n < 0:
#         print("Incorrect input")
#         # First Fibonacci number is 0
#     elif n == 1:
#         return 0
#     # Second Fibonacci number is 1
#     elif n == 2:
#         return 1
#     else:
#         return Fibonacci(n - 1) + Fibonacci(n - 2)
#
# print(Fibonacci(5))


# def fibonacci(n):
#     if(n <= 1):
#         return n
#     else:
#         print("uuuuu",n-1,n-2)
#         return(fibonacci(n-1) + fibonacci(n-2))
# n = 8
# print("Fibonacci sequence:")
# for i in range(n):
#     s=(fibonacci(i),)
#     print(s)
#     print('xxxxx')

#fibonacci series using list comprehension:

# n=8
# fibonacci_list = [0,1]
# for k in range(2,n):
#      fibonacci_list.append(fibonacci_list[k - 1] + fibonacci_list[k - 2])
#      print(k - 1, k - 2,)
#      print(fibonacci_list)
#
# # print([fibonacci_list.append(fibonacci_list[k-1]+fibonacci_list[k-2]) for k in range(2,n)])
# print(*fibonacci_list)


#armstrong number
# n=153
# c=0
# for i in ((str(n))):
#     tmp=int(i)*int(i)*int(i)
#     c=c+tmp
# print(c)


#perfect number program - (1+2+3)==6
# n=6
# c=0
# for i in range(1,n):
#     if n%i==0:
#         c=c+i
# print(c)

#perfect numbers in a range
# n=100
# for i in range(2,n+1):
#     c=0
#     for j in range(1,i):
#         if i%j==0:
#             c=c+j
#     if c==i:
#         print (c)


#guess the number
# while 1:
#     n=int(input('Guess the correct number'))
#     if n==7:
#         print("you are guessed")
#         break
#     else:
#         print("try again")


#password valid checker

# def password_checker(pass_str):
#     num_check=[0,1,2,3,4,5,6,7,8,9]
#     sym_check=["@","#","$",'&']
#     small_alpha="abcdefghigklmnopqrstuvwxyz"
#     capital_alpha=small_alpha.upper()
#     tmp=[]
#     if len(pass_str)>=8:
#         for i in [num_check,sym_check,small_alpha,capital_alpha]:
#             for j in i:
#                 if str(j) in pass_str:
#                     tmp.append('True')
#                     break       #if atleast one value in each above checks in pass_str
#         else:
#             if len(tmp)==4 and all(tmp):      #checks "True" in all conditions
#                 return True
#             else:
#                 return False
#
#     else:
#         return False
#
#
# pass_str='Country@123'
# print (password_checker(pass_str))





#Anagram word
# a="listen"
# b="silent"
# a=list(sorted(a))
# b=list(sorted(b))
# print(a,b)
# if a==b:
#     print ('True-It is a Anagram')



#decreasing and increasing on every number with next number (also checks for consective numbers 123,145,789,379)
# a="32454659670768190"
# a=list(a)
# a=list(map(int,a))
# print(a)
# consective_num=3  #minimum three numbers
# for i in range((len(a)-consective_num+1)):
    # print(i,i+consective_num)
    # if a[i:i+consective_num]==list(sorted(a[i:i+consective_num])):
    #     print('Consective numbers matched--',i,a[i:i+consective_num])




#convert into binary number
# n=10
# f=[]
# while (n>1):
#     f.append(0) if n%2==0 else f.append(1)
#     n=n/2
# print (list(reversed(f)))


# Function to convert decimal number to binary using recursion
# def DecimalToBinary(num):
#     if num > 1:
#         print(num)
#         DecimalToBinary(num // 2)
#     print(num % 2,end="")
#
# dec_val = 24
#
# # Calling function
# DecimalToBinary(dec_val)


#print right side triangle
# n=5
# for i in range(1,n+1):
#     print ('*'*i)


# def perm(a, k=0):
#    if k == len(a):
#       print (a)
#    else:
#       for i in range(k, len(a)):
#          a[k], a[i] = a[i] ,a[k]
#          perm(a, k+1)
#          a[k], a[i] = a[i], a[k]
#
# perm([1,2,3])


#longest line in a file
# e=[]
# with open("sample.txt",'r+') as f:
#     for i,j in enumerate(f.readlines()):
#         e.append([i,len(j)])
# print (max(e,key=lambda x:x[1]))

#copy contents from one file into another file
# with open("sample.txt",'r+') as f:
#     with open ("sample123.txt",'r+') as f1:
#         f1.write(f.read())



#fetching numbers in a file
# import re
# with open("sample.txt",'r+') as f:
#     s=f.read()    #getting entire file data
# r=re.findall(r"\d{5,}",s)    #finding numbers atleast 5 digits
# print(r)


#categorize words by same last matching word - (using dictionary with last work as key is best method)
# test_list = ['an', 'apple', 'geek', 'sample','for','nan', 'greek','gor','free','seek']
# final=[]
# for i,j in (enumerate(test_list)):
#     tmp=[]
#     for k,l in (enumerate(test_list)):
#         print(i,j,k,l)
#         if i!=k:
#             if j[len(j)-1:]==l[len(l)-1:]:
#                 tmp.append(l)
#     tmp.insert(0,j)
#     final.append(tmp)
#     if tmp:
#         print(tmp)
#         for i in tmp:
#             test_list.remove(i)
# if test_list:
#     final=final+[test_list]   #some values are missing due to removing while iterations, so finally adding the original list
# print(final)   ##[['an', 'nan'], ['geek', 'greek', 'seek'], ['for', 'gor'], ['apple', 'sample', 'free']]


#finding maximum two numbers
# test_list = [3, 4, 1, 7, 9, 1]
# sum_max_num=test_list[0]+test_list[1]
# max_num_value1,max_num_value2=test_list[0],test_list[1]
# for i in range(1,len(test_list)):
#     for j in range(i+1,len(test_list)):
#         if (test_list[i]+test_list[j])>sum_max_num:
#             sum_max_num=(test_list[i]+test_list[j])
#             max_num_value1, max_num_value2 = test_list[i], test_list[j]
# print(max_num_value1,max_num_value2,sum_max_num)


# test_list = [0, 1, 2, 3, 4, 5]
# k=3
# tmp=[]
# try:
#     for i in range(len(test_list)):
#         s=test_list[test_list[i]:k]
#         # if len(s)==3:
#         print(s)
#         k=k+1
# except:
#     for j in range()
#
#     pass



#interate the indexes like#---(0,1,2),(1,2,3),(2,3,4),(3,4,5),(4,5,0),(5,0,1)

# test_list = [5,7,9,11,45,78]
#
# res = [((test_list[i]), test_list[(i + 1) % len(test_list)], test_list[(i + 2) % len(test_list)])   for i in range(len(test_list))]
# #gives the list values with indexes like -(0,1,2),(1,2,3),(2,3,4),(3,4,5),(4,5,0),(5,0,1)
#
# print("The triplet list is : " + str(res))    #[(5, 7, 9), (7, 9, 11), (9, 11, 45), (11, 45, 78), (45, 78, 5), (78, 5, 7)]
#



#Balance the opening and closing braces in a string:
# s="s)at((()hi)(s)())))(h(()"
# s=list(s)
# op=0
#
# for j,i in enumerate(s):
#     if i==')' and op==0:
#         s[j]='#'     #marking the items as '#' to delete outside for loop. (if we delete directly inside for loop, some adajcent list items we will miss to delete in iteration)
#     elif i=='(':
#         op=op+1
#     elif i==')':
#         op=op-1
#
# d=list(filter(lambda x:x!='#',s))      #creating a new list, omitting the '#' values
# print(d)
#
# for i in range(op):
#     d.append(')')      #adding the closing bracekets for extra open braces to balance
#
# print(d)
# print(d.count('('),d.count(')'))



# test_str = 'geeksforgeeeks'
# g=[]
# word='e'
# print(test_str.find('e'))
# for j,i in enumerate(test_str):
#     count = 1
#     if i==word:
#         for k in range(j+1,len(test_str)):
#             if test_str[k]==word:
#                 count=count+1
#             else:
#                 break
#         g.append(count)
#     else:
#         continue
#
# print(g)


# test_str = 'geeksforgeeeks'
# i=0
# tmp=[]
# while i<len(test_str):
#     if test_str[i]=='e':
#         # print (test_str.find('e'))
#         tmp.append(i)
#     i=i+1
# print(tmp)
# numbers=[]
# for j in range(len(tmp)-1):
#     if tmp[j]-tmp[j+1]==-1:
#         numbers.append([tmp[j],tmp[j+1]])
# print(numbers)


#Skipping For iterations using iter() and next()
# song = ['always', 'look', 'on', 'the', 'bright', 'side', 'of', 'life']
# song_iter = iter(song)
# for sing in song_iter:
#     print ("gggg",sing)
#     if sing == 'look':
#         next(song_iter)         #calls next for loop iteration, so we skipping three for loop iterations.
#         next(song_iter)
#         next(song_iter)
#         print ('a---' + next(song_iter))    #printing the next for loop iteration


#armstrong number using sum()
# n='153'
# if int(n)==(sum(int(i)*int(i)*int(i) for i in str(n))):
#     print('armstrong')


#program to find LCM

# def lcm(x, y):
#     if x > y:
#        greater = x
#     else:
#        greater = y
#     while(True):
#        if((greater % x == 0) and (greater % y == 0)):
#            lcm = greater
#            break
#        greater += 1
#     return lcm
#
#
# print(lcm(60,48))






# Python code to find GCD for two numbers

# def computeGCD(x, y):
# 	if x > y:
# 		small = y
# 	else:
# 		small = x
# 	for i in range(1, small + 1):
# 		if ((x % i == 0) and (y % i == 0)):
# 			gcd = i       # 12 is the last maximum common divisor for 60 and 48, so returns 12
#
# 	return gcd
#
# a = 60
# b = 48
#
# print("The gcd of 60 and 48 is : ", end="")
# print(computeGCD(60, 48))

#converting into one number
# test_list = [6, 8, 4, 9, 10, 2]
# d=list(map(str,test_list))
# print (int("".join(d)))    #6849102



#removes internal lists
# test_list = ([6], [8], [4], [9], [10], [2])
# e=[]
# for i in test_list:
#     e=e+i   #can use extend() also
# print(e)     #[6, 8, 4, 9, 10, 2]


#counting the letters using dict setdefault
# f="sathish"
# g={}
# for i in f:
#     g.setdefault(i,0)
#     print (g)
#     g[i]=g[i]+1
# print(g)     #{'s': 2, 'a': 1, 't': 1, 'h': 2, 'i': 1}




#converts nested dictionary into normal dictionary
# test_dict = {'gfg' : {'a' : 15, 'b' : 14},
#              'is' : {'d' : 2, 'e' : 10, 'f' :  3},
#              'best' : {'g' : 19}}
# d={}
# for key,value in test_dict.items():
#     if isinstance(value,dict):
#         for i,j in value.items():
#             d.update([(i,j)])
# print(d)     #{'a': 15, 'b': 14, 'd': 2, 'e': 10, 'f': 3, 'g': 19}


# getting all keys from nested dictionary
# test_dict = {'gfg': 43, 'is': {'best' : 14, 'for' : 35, 'geeks' : 42}, 'and' : {'CS' : 29}}
# d=set()    #using set() to avoid duplicates key
# print(len(test_dict))
# for key,val in test_dict.items():
#     if isinstance(val,dict):
#         d.add(key)
#         d.update(val.keys())
#     else:
#         d.add(key)
# print(d)    #{'for', 'is', 'geeks', 'and', 'best', 'gfg', 'CS'}



# test_dict = {'gfg' : [4, 6,"jjj",8],'p':'567', 'is' : (9, 8, 2),'eee':'fff', 'best' : [10, 3, 2],'ww':{1:2,4:88}}
# s=test_dict.values()
# final_values=[]
# for i in s:
#     if isinstance(i,list) or isinstance(i,tuple):
#         for j in i:
#             try:
#                 final_values.append(int(j))
#             except Exception as err:
#                 print(err)
#     elif isinstance(i,int):
#         final_values.append(i)
#     elif isinstance(i,dict):
#         for k in i.values():
#             try:
#                 final_values.append(int(k))
#             except Exception as err:
#                 print(err)
# print(final_values)





#If finally is defined, we can’t return in mid-way
# def a(z):
#     try:
#         return 333     #return will not work
#         100/z
#     except ZeroDivisionError:
#         return 444            #return will not work
#     finally:
#         return 1        #return works
#
# print(a(0))



# def step_1():
#     return True
#
# if step_1():    #checks above function returns True
#     print('ggg')

#for loop iterations running from int(input())
# for i in range(int(input())):
#     print(i)


#removing nested dict "none" values
# test_dict = {'gfg' : {'a' : 1, 'b' : 2},
#               'is' : {'d' : None, 'e' : None},
#               'best' : {'g' : 1}}
#
# d=[]
#
#
# for j,i in test_dict.items():
#     if isinstance(i,dict):
#         for x,y in i.items():
#             if y==None:
#                 d.append([j,x])
# print(test_dict)
#
# if d:
#     for i,j in d:
#         del test_dict[i][j]    #can't delete dict values during above for loop in runtime, so deleting here separetly
#
# print(test_dict)






#generator program for fibonacci
# def fib(limit):
#     # Initialize first two Fibonacci Numbers
#     a, b = 0, 1
#
#     while a < limit:
#         yield a
#         a, b = b, a + b
#
# print("\nUsing for in loop")
# for i in fib(5):  #Technically, we calling the above function once fib(5), whenerver above 'yield a' it returns to this for loop and prints that value
#                  # and again goes back into function's while loop, because still it under range '5' only.
#     print(i)


#program to change first and last letter of every word into capital letter
# d='sat How was today'
# q=[]
# f=d.split()
# for i in f:
#     if i.isalpha():    #passes only string
#         if len(i)==1:
#             q.append(i[0].upper())
#         elif len(i)==2:
#             q.append(i[0].upper())
#             q.append(i[-1].upper())
#         else:
#             q.append(i[0].upper())
#             for j in range(1,len(i)-1):
#                 q.append(i[j])
#             q.append(i[-1].upper())  #last letter of every word
#         q.append(' ')
#
# print("".join(q))   #SaT HoW WaS TodaY


#to get the second largest combination of numbers from list
# v=[10,20,30,40,50]
#
# def largest_combination(w=2):
#     d=sorted(v,reverse=True)
#     return (d[0],d[w])
#
# print(largest_combination(2))     #(50,30) -  second largest combination


#using mutuable objects list,dictionary for storing particular objects data self.dictionary, self.list
# class A:
#     def __init__(self):
#         self.data={}
#
#     def enter_data(self,data,value):
#         self.data[data]=value
#
#     def display_data(self):
#         print (self.data)
#
# x=A()
# y=A()
# x.enter_data(1,2)
# y.enter_data(3,4)
# x.display_data()

#static functions and static variables working in inheritance subclasses
# class A:
#     q='sat'
#     @staticmethod
#     def ad():
#         print (234)
#
# class B(A):
#     pass
#
# f=B()
# f.ad()
# print(f.q)



#
#
# print ({i:("True" if i%2==0 else "False") for i in range(1,11)})
#
# print ({("True{}".format(str(i)) if i%2==0 else "False{}".format(str(i))):i for i in range(1,11)})

#counts the words in list
# my_list = ['hello', 'hi', 'hello', 'today', 'morning', 'again', 'hello']
# my_dict = {k:my_list.count(k) for k in my_list}
# print(my_dict)    #{'hello': 3, 'hi': 1, 'today': 1, 'morning': 1, 'again': 1}



#implements 'elif' in list comprehension
# l = [1, 2, 3, 4, 5]

# for values in l:
#     if values==1:
#         print ('yes')
#     elif values==2:
#         print ('no')
#     else:
#         print ('idle')

# print(['yes' if v == 1 else 'no' if v == 2 else 'idle' for v in l])   #does the same from above code.


#nested list comprehensions --  prints list of lists
# rows = ([1, 2, 3], [10, 20, 30])
# print([[j-1 for j in i] for i in rows])
#
# print([[x for x in range(10) if x%2==i] for i in range(2)])

#print([[0 for j in range(3)] for i in range(3)]) # 3X3 0 MAtrix


#nested dictionary comprehension
# print ({i:{i:("True" if i%2==0 else "False")} for i in range(5)})
#
# print ({i:{j:['sss'] for j in range(5)} for i in range(5)})




#program for two matrix addition/substration/division/multiply in same size
# X = [[1, 2, 3,0],
# 	 [4, 5, 6,0],
# 	 [7, 8, 9,0]]
#
# Y = [[9, 8, 7],
# 	 [6, 5, 4],
# 	 [3, 2, 1]]
#
#
#
# result = [[0,0,0],
#         [0,0,0],
#         [0,0,0]]

# # iterate through rows
# for i in range(len(X)):
# 	# iterate through columns
# 	for j in range(len(X[0])):
# 		result[i][j] = X[i][j] + Y[i][j]
#
# for r in result:
# 	print(r)

#
# print ([[X[i][j]+Y[i][j] for j in range(len(X[0]))] for i in range(len(X))])   #using list comprehension
#



#program for finding LCM for one number, always returns same number, which is correct. (below while-for loop logic reference)
# def fff(num):
# 	for i in range(2,int(num+1)):
# 		if num%i==0:
# 			return i
#
# n=60
# c=1
# while n>1:
# 	r=fff(n)
# 	c=c*r
# 	n=n/r
#
# print(c)


s="aeccdhba"
print(ord('a'))


#program to iterate and gets value from nested lists using recursion
# text = [u'sam', [['Test', [['one', [], []]], [(u'file.txt', ['id', 1, 0])]], ['Test2', [], [(u'file2.txt', ['id', 1, 2])]]], []]
# text = [['Test2',[(u'file2.txt', ['id', 1, 2])]]]
# def get_values(lVals):
#     print(lVals)
#     res = []
#     for val in lVals:
#         if type(val) not in [list, set, tuple]:
#             res.append(val)
#         else:
#             res.extend(get_values(val))
#     return res
#
# a=get_values(text)
# print(a)     #['Test2', 'file2.txt', 'id', 1, 2]


#summation of list using recursion
# def list_sum(val):
#     if len(val)==1:
#         return val[0]
#     return val[0]+list_sum(val[1:])
#
# print(list_sum([2, 4, 5, 6, 7]))




#summation of nested list using recursion
# def nested_sum(val):
#     print(val)
#     total=0
#     for i in val:
#         if type(i) not in [list]:
#             total=total+i
#         else:
#             total=total+nested_sum(i)
#
#     return total
#
# print((nested_sum([1, 2, [3,4], [5,6]])))   #prints 21


#string into nested dictionary using recursion
# def nested_dict(val):
#     if len(val)==1:
#         # return {val[0]:""}
#         return val[0]     # 'h'
#     return {val[0]:nested_dict(val[1:])}
#
#
# s='sathish'
# print(nested_dict(s))    #{'s': {'a': {'t': {'h': {'i': {'s': 'h'}}}}}}



#parallely combines two list into dictionary
# test_list1 = ['Nikhil', 'Akash', 'Akshat']
# test_list2 = [5, 6, 7, 8, 2, 3, 12, 2, 10]
# d=0
# f={}
# len_list=len(test_list2)//len(test_list1)   #calculating slicing length
# for i in test_list1:
#     f[i]=test_list2[d:d+len_list]
#     d=d+len_list
# print(f)    #{'Nikhil': [5, 6, 7], 'Akash': [8, 2, 3], 'Akshat': [12, 2, 10]}




#program to get the number of consective strings in one string/one list

# last = ''   #dummy value to get into 'else' condition for first letter
# results = []
# word = 'assassin'
# for letter in word:
#     if letter == last:
#         results[len(results)-1] = (letter, results[len(results)-1][1] + 1)   #if consective string, increase the last recent letter by one
#     else:
#         results.append([letter, 1])     #No consective, enters letter into one occurance
#         last = letter
#
# print(results)    #[['a', 1], ('s', 2), ['a', 1], ('s', 2), ['i', 1], ['n', 1]]
#
# print ((list(sorted(results,key=lambda x:x[1],reverse=True))))    #prints the count occurance in descending order



#finding missing numbers from min/max values range
# d=[4,2,6,7,8,10]
# print([i for i in range(min(d),max(d)) if i not in d])   #[3,5,9]



# Python program to print all permutations with
# duplicates allowed

# def toString(List):
# 	return ''.join(List)
#
# # Function to print permutations of string
# # This function takes three parameters:
# # 1. String
# # 2. Starting index of the string
# # 3. Ending index of the string.
# def permute(a, l, r):
# 	if l == r:
# 		print (toString(a))
# 	else:
# 		for i in range(l, r + 1):
# 			a[l], a[i] = a[i], a[l]
# 			permute(a, l + 1, r)
# 			a[l], a[i] = a[i], a[l] # backtrack
#
# # Driver program to test the above function
# string = "ABC"
# n = len(string)
# a = list(string)
# permute(a, 0, n-1)



# def permute_string(str):
#     if len(str) == 0:
#         return ['']
#     prev_list = permute_string(str[1:len(str)])
#     print("&&&&",prev_list)
#     next_list = []
#     for i in range(0,len(prev_list)):
#         for j in range(0,len(str)):
#             new_str = prev_list[i][0:j]+str[0]+prev_list[i][j:len(str)-1]
#             # print(new_str)
#             if new_str not in next_list:
#                 next_list.append(new_str)
#     return next_list
#
# print(permute_string('ABCD'));



# def permute(list, s):
#     if list == 1:
#         return s
#     else:
#         return [ y + x
#                  for y in permute(1, s)
#                  for x in permute(list - 1, s)
#                  ]
#
# print(permute(1, ["a","b","c"]))
# print(permute(2, ["a","b","c"]))


class WrittenText:

	"""Represents a Written text """

	def __init__(self, text):
		self._text = text

	def render(self):
		return self._text

class UnderlineWrapper(WrittenText):

	"""Wraps a tag in <u>"""

	def __init__(self, wrapped):
		self._wrapped = wrapped

	def render(self):
		return "<u>{}</u>".format(self._wrapped.render())

class ItalicWrapper(WrittenText):

	"""Wraps a tag in <i>"""

	def __init__(self, wrapped):
		self._wrapped = wrapped

	def render(self):
		return "<i>{}</i>".format(self._wrapped.render())

class BoldWrapper(WrittenText):

	"""Wraps a tag in <b>"""

	def __init__(self, wrapped):
		self._wrapped = wrapped

	def render(self):
		return "<b>{}</b>".format(self._wrapped.render())

""" main method """

if __name__ == '__main__':

	before_gfg = WrittenText("GeeksforGeeks")
	after_gfg = ItalicWrapper(UnderlineWrapper(BoldWrapper(before_gfg)))

	print("before :", before_gfg.render())
	print("after :", after_gfg.render())



#Download a large file using requests
# import requests
# url="https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv"
# response = requests.get(url, stream = True)
#
# text_file = open("data.txt","wb")
# for chunk in response.iter_content(chunk_size=1024): #stream = True, enables to (iter_content) iterate a large content in chunks in a open requests connection
#     text_file.write(chunk)
# text_file.close()



#Program ----- similarly for uploading files also, first should read a file and then write the readed content
# input_file = open('input-file_path', 'wb')
# output_file = open('output-file_path', 'wb')
# input_file.seek(0)    #changing cursor position to start of file
# while 1:
# 	data = input_file.read(1024)   #reads content as 1024 bytes
# 	if not data:
# 		break
# 	output_file.write(data)
# input_file.close()
# output_file.close()