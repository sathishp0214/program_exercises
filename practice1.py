

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


#stores only the non-repeated letters in each word in same order (without using set)
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
#     print(i,i+consective_num)
#     if a[i:i+consective_num]==list(sorted(a[i:i+consective_num])):
#         print('Consective numbers matched--',i,a[i:i+consective_num])




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


# s="aeccdhba"
# print(ord('a'))


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
#         results[len(results)-1] = [letter, results[len(results)-1][1] + 1]   #if consective string, increase the last recent letter by one
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


# class WrittenText:
#
# 	"""Represents a Written text """
#
# 	def __init__(self, text):
# 		self._text = text
#
# 	def render(self):
# 		return self._text
#
# class UnderlineWrapper(WrittenText):
#
# 	"""Wraps a tag in <u>"""
#
# 	def __init__(self, wrapped):
# 		self._wrapped = wrapped
#
# 	def render(self):
# 		return "<u>{}</u>".format(self._wrapped.render())
#
# class ItalicWrapper(WrittenText):
#
# 	"""Wraps a tag in <i>"""
#
# 	def __init__(self, wrapped):
# 		self._wrapped = wrapped
#
# 	def render(self):
# 		return "<i>{}</i>".format(self._wrapped.render())
#
# class BoldWrapper(WrittenText):
#
# 	"""Wraps a tag in <b>"""
#
# 	def __init__(self, wrapped):
# 		self._wrapped = wrapped
#
# 	def render(self):
# 		return "<b>{}</b>".format(self._wrapped.render())
#
# """ main method """
#
# if __name__ == '__main__':
#
# 	before_gfg = WrittenText("GeeksforGeeks")
# 	after_gfg = ItalicWrapper(UnderlineWrapper(BoldWrapper(before_gfg)))
#
# 	print("before :", before_gfg.render())
# 	print("after :", after_gfg.render())



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


# import urllib.request
# from concurrent.futures import ThreadPoolExecutor
# urls = [
#   'http://www.python.org',
#   'https://docs.python.org/3/',
#   'https://docs.python.org/3/whatsnew/3.7.html',
#   'https://docs.python.org/3/tutorial/index.html',
#   ]
#
# # with ThreadPoolExecutor(2) as executor:   #executer variable manages the 4 threads internally
# #     results = executor.map(urllib.request.urlopen, urls)
# #
# # # print("rrrr",list(results))
# # for i in list(results):
# # 	print(list(i))



# from multiprocessing.pool import ThreadPool
#
#
# with ThreadPool(2) as executor:   #executer variable manages the 4 threads internally
#     results = executor.map(urllib.request.urlopen, urls)
# 	# executor.
#
# # print("rrrr",list(results))
# for i in list(results):
# 	print(list(i))
#
#
#
# def f(x):
#     print(x)
#     return x*x
#
# if __name__ == '__main__':
#     with ThreadPool(2) as pool:         # start 4 worker processes
#         # result = pool.apply_async(f,(10,))
# # evaluate single value "f(10)" asynchronously in a single process
# #         print(result.get())        # prints "100"
#
#         r=((pool.map_async(f, range(10))))
#         print(r.get())



# try:
#     a=12
#     d=2/0
# except Exception as err:
#     raise (err)     #instead of print error message, raising exception with error message
#     print('gggg')   #this line will not be executed


#program to compare > < the alphabets

# s='f'
# if 'e' < s[0] <= 'm':
#     print ('fff')
# if s[0]>'e' and s[0]<'m':
#     print('ttt')
# if s[0]>'b':
#     print ('gggg')



#prints only non-repeated characters
# s='sathish'
# t=[]
# for i in s:
#     if i not in t:
#         t.append(i)
#     elif i in t:
#         t.remove(i)
# print(t)   #['a', 't', 'i']


#program to check every character is a digit
# s='p123'
# print(all(ord(i) in range(48,58) for i in s))   #False    #using range of ascii value for numbers 0-9


#square root of program
# num=100
# for i in range(2,num//2):
#     if i*i==num:
#         print(i)     #10
#         break


# #program to find count the numbers
# a=[[100, 300], [145, 215], [200, 230,234], [215, 300], [215, 400,567,234], [500, 600], [600, 700]]
# print(sum(len(i) for i in a))   #17



#Prints values between the range of values
# a=[[100, 300], [145, 215], [200, 230,234], [215, 300], [215, 400,567,234], [500,450, 600], [600, 700]]
# b=[j for i in a for j in i]
# c=(list(sorted(b)))    #sorting the values for easy calculation
# r=420
# try:
#     for i,j in enumerate(c):
#         if r in range(c[i],c[i+1]):
#             print((c[i],c[i+1]))    #(400, 450)   #420 value present in this range
#             break
# except:
#     pass


#both while and if condition, doesn't accepts "" empty string without spaces in 'TRUE' case
# while "":
#     print ('hhh')
# else:
#     print ('gggg')    #prints 'gggg


# t = "bacdcba"
# f=[]
# e="increase" if ord(t[0])<ord(t[1]) else 'decrease'



#program to check no duplicate numbers using function
# def duplicate_number(p):
#     che=[]
#     for i in p:
#         if i not in che:
#             if p.count(i)>1:
#                 return ("Duplicates numbers are present")
#     return True
#
# d = "9831"
# p = list(d)
# print(duplicate_number(p))

#using set to find duplicate numbers
# s="98391"
# f=list(s)
# d=set(s)
# if len(f)==len(d):
#     print("No duplicate numbers")

# print(sorted(f),sorted(d),sorted(s))   #['1', '3', '8', '9'] ['1', '3', '8', '9'] ['1', '3', '8', '9']





#Program to print the divisors of numbers with two digits or three digits etc
# def num_of_digit_divisors(num,start_num,end_num):
#     result=[]
#     for i in range(start_num,end_num):
#         if i%num==0:
#             result.append(i)
#     return result
#
#
# num=7
# digits=2
# start_num=pow(10,digits-1)   #start_range
# end_num=pow(10,digits)   #end_range
# print(start_num,end_num)
# print(num_of_digit_divisors(num,start_num,end_num))   #[14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]  #prints divisors of '7' numbers in two digits




#program to longest palindrome in the substring
# s='bananas'
# s='forgeeksskeegfor'
# final=len(s) - 1
# for i in range(1,len(s)-1):
#     tmp=s[i:final]
#     # print(tmp)
#     if len(tmp)>=3:
#         if tmp==tmp[::-1]:
#             print("longest palindrome in substring:",tmp)   #geeksskeeg
#             break
#     final=final-1



#insert the substring in string using slicing
# r='sathish'
# insert=3
# insert_string='555'
# print(r[:insert]+insert_string+r[insert:])   #sat555hish



#checks mirror matrix or not
# def mirrorMatrix(mat1,mat2,N):
#     for i in range(N):
#         k=0
#         for j in range(N-1,-1,-1):
#             print(mat1[i][j],"____",mat2[i][k])
#             if mat1[i][j] != mat2[i][k]:      #checks 1st ans 2nd matrix column values
#                 return ("Not a mirror matrix")
#             k=k+1    #checks the second matrix column indexes
#     return ("mirror matrix")
#
#
#
#
#
# N = 3
# mat1 = [[1, 2, 3],
#         [0, 6, 7],
#         [9, 10, 11]]
#
# mat2 = [[3, 2, 1],
#         [7, 6, 0],
#         [11, 10, 9]]
#
# # Function call
# print(mirrorMatrix(mat1, mat2, N))



#program to right_shift and left_shift of string
# def shift_numbers(string,right_shift,left_shift):
#     if right_shift==left_shift:    #if both right_shift and left_shift are same, going to get same string after shifting, so simply returned it
#         return string
#
#     if right_shift>len(string):    #if right shift or left shift greater than length of string, getting the remainder as new right shift and left shift
#         right_shift=right_shift%len(string)
#
#     if left_shift > len(string):
#         left_shift = left_shift % len(string)
#
#     print(right_shift,left_shift)
#     right_index = len(s) - right_shift
#     tmp = s[right_index:] + s[:right_index]
#     tmp1 = tmp[left_shift:] + tmp[:left_shift]
#     return (tmp, tmp1)
#
# s='abcdef'
# right_shift=40
# left_shift=39
#
# print(shift_numbers(s,right_shift,left_shift))


#Program to print index occurances of substring with multiple substring occurances
# index_list=[]
# string = "test test test test"
# sub_string='test'
# start=0
# while 1:
#     tmp=string.find(sub_string,start)    #find() inbuilt additional 'start' index parameter
#     print(tmp)
#     if tmp==-1:
#         break
#     index_list.append(tmp)
#     start=start+len(sub_string)    #transvering the next substring starting index
#
# print(index_list)   #[0, 5, 10, 15]   #'test' substring indexes are


#using regex finditer() to substring index(similar to above program)
# import re
# x = 'banananassantana'
# s=re.finditer('na', x)
# for i in s:
#     print(i.start())   #2 4 6 14  "na" substring index in this string



#even empty and false values are taken inside list
# s=[1,2,3,[],(),False]
# print(len(s))    #prints 6, even empty and false values are taken


#break - Break works only on current for/while loop, (not the parent for loop)
# for j in range(3):
#     print(j)
#     for k in range(4):
#         print('k',k)
#         if k==1:
#             if 1:
#                 if 1:
#                     if 1:
#                         break   #even multiple nested if statements, still this 'breaks' works for 'k for loop'



#finding common and uncommon values between two lists/tuples/sets

# a={1,2,3}
# b={2,3,4}
# print(b.intersection(a))   #{2, 3}
# print(b.difference(a))   #{4}   #4 is uncommon compare to set 'a'



#Using recursion, run the child 'for loop' 'n' iteration times
# def looping(n):
#     if n==0:
#         return
#     looping(n - 1)     #child for loop for 4 iterations for
#     for i in range(3):    #parent for loop - 3 iterations
#         print(i,n, end=" ")
#         print("---------")
#
# # 0 1 ---------
# # 1 1 ---------
# # 2 1 ---------
# # 0 2 ---------
# # 1 2 ---------
# # 2 2 ---------
# # 0 3 ---------
# # 1 3 ---------
# # 2 3 ---------
# # 0 4 ---------
# # 1 4 ---------
# # 2 4 ---------
#
# child_for_loop_times=4
# looping(child_for_loop_times)


#using exception with "pass", for breaking all for loops
#using exception with "raise", for breaking all while loops - (because 'break' just quits the current loop not all parent loops)
#--"Another method" - inside a function, we can return it

# try:
#     for a in range(5):
#         for b in range(5):
#             if a==3 and b==3:
#                 raise StopIteration
#             print (b)
# except StopIteration:
#     # raise          #while loops we should 'raise'
#     pass

#inbuilt abs() - converts negative number into positive number
# w=(abs(-23.05))
# print(w+10)   #33.05




#swapping the values with depends upon input
#random number generation within range - Ex: range(12,34) #if we swapping with '2' input, it swaps more numbers

# def swapping_on_input(input,swap_number):
#     print(input)
#     if swap_number>=len(input):
#         return False
#     try:
#         for i in range(0,len(input)-1,swap_number):
#             print(i,i+swap_number)
#             input[i],input[i+swap_number]=input[i+swap_number],input[i]
#     except Exception as err:
#         print(err)
#     return input
#
# w=[10,20,30,40,50,60,70]
#
# print(swapping_on_input(w,3))
#
# print(swapping_on_input(list(range(12,34)),2)) #random number generation within range  #[14, 13, 16, 15, 18, 17, 20, 19, 22, 21, 24, 23, 26, 25, 28, 27, 30, 29, 32, 31, 12, 33]



#program to check "input list has only one value with multiple occurances"
# p=[3, 3, 4, 3, 3]
# p=[9,9,9,9]
# tmp=[p[0]]*len(p)
# print(p,tmp)
# if p==tmp:
#     "input list has only one value with multiple occurances"



#returns the sublist- repeating cocuurances
# def sublist_occurance(input_list):
#     result={}
#     # while len(input_list)>1:
#     j = 0
#     try:
#         tmp= input_list.index(input_list[0],1)   #if value is not repeated, raising exception
#         result[tmp]=[]
#         for i in range(tmp,tmp*2):    #runs iteration from repeating number finding index and length of repeating number
#             if input_list[j]==input_list[i]:
#                 result[tmp].append(input_list[i])
#                 j=j+1
#             else:
#                 # input_list=input_list[i:]
#                 break
#         return result
#     except ValueError as Err:
#         raise (Err)
#
#
#
#
# input_list=[1, 2, 3, 3, 1, 2, 3,3]
# input_list=[ 1, 2, 2, 1, 2, 2, 1, 2, 2 ]   #{3: [1, 2, 2]}   #3- repeat starting index
# print(sublist_occurance(input_list))     #{4: [1, 2, 3, 3]}



#Finds remainder carry from two binary numbers
#
# num1 = 14
# num2 = 12
# num1=list(bin(num1).lstrip('0b'))
# num2=list(bin(num2).lstrip('0b'))
# print(num1,num2)
# flag=0
# for i in range(3,-1,-1):   #checking from reverse position
#     if num1[i]=='1' and num2[i]=='1':
#         flag=flag+1
#     if (num1[i]=='0' and num2[i]=='0') and flag>0:
#         flag=flag-1
# print(flag)    #2    #carry is 2


#Minimum steps to taken a value into zer value Ex: 21 into 0

# n=21
# flag=0
# while n>0:
#     if n%3==0:
#         flag=flag+1
#         n=n/3
#     elif n%2==0:
#         flag=flag+1
#         n=n/2
#     else:         #if number is not divisible in both 2 and 3, reducing value by 1 and adding flag value
#         n=n-1
#         flag=flag+1
# print(flag)    #5 totally 5 steps ---->  #21/3 =7 then 7-1=6 then 6/3 =2 then 2/2=1 then 1-1=0


#program to check all list are increasing/decreasing using all()

#another method - using sorting input list sorted() and checks compares with the input.

# def strictly_increasing(L):
#     return all(L[x]<L[x+1] for x in range(len(L)-1))
#
# L=[1,2,3,4,5]
# print(strictly_increasing(L))



#program to reduce the elements into zeros with how many steps

# s=[1, 2, 3, 2, 1]    #3 --> three steps all elements gets zero
# s=[5, 4, 3, 4, 4]    #5 --->five steps all elements gets zero
# k=0
# while 1:
#     if s.count(0)==len(s):    #checks all elements are zero
#         break
#     for i in range(len(s)):
#         if s[i]>0:
#             s[i]=s[i]-1
#     print(s)
#     k=k+1
#
# print(s,"How many steps:",k)   #[0, 0, 0, 0, 0] How many steps: 5


# print(int('1111',2))    #Converts binary into decimal number with int() inbuilt


##Converts binary into decimal number with for loop logic
# bianry_range=[1,2,4,8,16,32,64,128]
# num='1100'
# num=list(reversed(num))
# sum=0
# for i in range(len(num)):
#     if num[i]=='1':
#         sum=sum+bianry_range[i]
# print(sum)


# print(bin(0b1000 * 0b1010))   #binary multiplication
#
# print(bin(0b1000 * 3))    # '3' binary number was automatically used and doing multiplication
#
#
# print(bin(0b1000 + 0b1010))   #binary addition
#
# print(bin(15+10))  #binary addition



#while loop with exception handling
# i=0
# try:
#     while True:
#         if i==8:
#             raise StopIteration
#         print(i)
#         i = i + 1
# except Exception:
#     raise     #without 'raise' , will not break the while loop, run continuously.
# else:
#     pass
# finally:
#     print("task completed")



# elements alternate increasing and decreasing  --- If we want alternate decreasing and increasing(changes the signs >,<) with seperate function

# def increasing_and_decreasing(a):
#     for i in range(0,len(a)-2,2):   #iterate into '2', because we checking three elements at once in below if condition
#         # print(i)
#         if not (a[i]<a[i+1]>a[i+2]):
#             return False
#     return True
#
# a=[3,4,2,5,2,7,1]
# a=[2,3,4,1]
#
# print(increasing_and_decreasing(a))



#remove (k=2) upto two smallest characters in a string:

# string="jackie"
# k=2
# sub_string=sorted(string)[:k]   #gets 2 smallest characters
# print(sub_string)
# for i in sub_string:
#     string=string.replace(str(i),'')   #replaces with the original string
# print(string)   #jkie



#finds minimum distance character from input
# d=['e','g','t','y']
# val='u'
# val=ord(val)
# k=[abs(val-ord(i)) for i in d]   #abs() --> converts negative value into positive value
# minimum_value=min(k)   #finiding minimum ascii value
# print(d[k.index(minimum_value)])   #prints 't' --->'t' is nearest character(minimum distance between 'u' input)




#swap the even numbers into even indexes  (assume have enough even numbers for the even indexes)
# d=[2, 4, 8, 3, 1,2,3]     #[2, 1, 8, 3, 4, 3, 2]
# # d=[11,3,4,8,2,10,13]     # output  [8, 3, 4, 11, 2, 13, 10]
# j=1
# for i in range(0,len(d),2):
#     if d[i]%2 != 0:
#         for j in range(1,len(d),2):    #just finding one even number in odd indexes and swap and then breaks
#             if d[j] %2 == 0:
#                 d[i],d[j]=d[j],d[i]
#                 break
#
# print(d)



#finds consective next numbers in the sequence
# nums= [0,3,4,5,6,7,10,11,12,14,98,99,100]
# result=[]
# tmp=[]
#
# for t in list(zip(nums, nums[1:])):   #This 'zip' prints as (0,3) , (3,4), (5,6)
#     if t[0]+1==t[1]:
#         tmp.extend(t)    #tmp list adds only consective next numbers
#     else:
#         if tmp:    #if consective next numbers fails, adds the numbers in result list
#             result.append(set(tmp))    #eliminates number duplicates
#             tmp=[]   #again making tmp list as empty list
#
# if tmp:   #if consective next numbers at the end of inputs Ex: 98,99,100, that case handles here
#     result.append(set(tmp))
#
# print((result))     #[{3, 4, 5, 6, 7}, {10, 11, 12}, {98, 99, 100}]
# print(max(result,key=len))    #{3, 4, 5, 6, 7}  -- longest sequence


#prints consective name numbers/string

# val='3255544132777634999'   ##['555', '44', '777', '999']
# val='sattthhppWWrt'    #['ttt', 'hh', 'pp', 'WW']
# val='AAAAABBCCCCCDDDCCCBBA'   #['AAAAA', 'BB', 'CCCCC', 'DDD', 'CCC', 'BB']
# result=[]
# tmp=[]
# i=0
# while i<len(val)-1:
#     # print(val[i])
#     if val[i]==val[i+1]:
#         tmp.extend([i,i+1])   #adds the consective elements indexes
#     else:
#         if tmp:
#             print('tmp',tmp)
#             p=set(tmp)
#             result.append(val[i]*len(p))    #prints the respected value with multiplication of length (set of indexes)
#             tmp=[]
#             d={}
#     i=i+1
#
# if tmp:   #if consective elements at the end of inputs
#     p = set(tmp)
#     result.append(val[i] * len(p))
#
# print(result)   #['555', '44', '777', '999']



#splitting elements with the number and prints the combination of two numbers
# input_value=[2,5,1,3,4,7]
# n=3
# val1=input_value[:n]
# val2=input_value[n:]
# print(val1,val2)
# result=[]
# for i,j in list(zip(val1,val2)):
#     result.extend([i,j])
# print(result)    #[2, 3, 5, 4, 1, 7]




#reverse the words only,(not the entire sentence) (without using lists)
# e='hello world how$ are you'   #olleh dlrow $woh era uoy
# tmp=''
# for i in e:
#     if not i.isspace():
#         tmp=tmp+i
#     else:
#         if tmp:
#             print(tmp[::-1],end=' ')
#             tmp=''
# if tmp:
#     print(tmp[::-1])    #olleh dlrow $woh era uoy




#form the dictionary with uneven keys and values list.
# test_list = ["Gfg", 3, "is", 8, "Best", 10, "for", 18, "Geeks", 33,78,'hhhh']

# key_list = ["name", "number", "sample"]
#
# length=len(test_list)//len(key_list)
#
# d=[]
# a=0
#
# for i in range(length):   #iteration for length of two input lists
#     tmp=test_list[a:a+len(key_list)]   #slicing into length of key list for zip()
#     d.append((dict(zip(key_list,tmp))))
#     a=a+len(key_list)
#
# print(d)  #[{'name': 'Gfg', 'number': 3, 'sample': 'is'}, {'name': 8, 'number': 'Best', 'sample': 10}, {'name': 'for', 'number': 18, 'sample': 'Geeks'}, {'name': 33, 'number': 78, 'sample': 'hhhh'}]



#without any consecutive 0’s and at most K consecutive 1’s
# N = 5
# M = 14
# K = 3
# a=M//K
# b=M%K   #gets remainder 2, 14%3 --> 2
# output_string=""
# for i in range(a):
#     output_string=output_string+'0'
#     output_string=output_string+ "1"*K
# print(len(output_string))
# if b>0:    #if remainder, it will add the remaining 0 and 1
#     output_string = output_string + '0'
#     output_string = output_string + "1" * b
#
# print(output_string)   #0111011101110111011 - N=5 -- 5 "0" should be placed between of 14 1's M=14, K=3 -- means consuctive 3 '1'



#prints the sequence
# a=0
# b=1
# for i in range(10):
#     c=(a+b)
#     print(c,end=",")  #1,3,6,10,15,21,28,36,45,55,
#     a=c
#     b=b+1




#same above sequence using recursion
# def recursive_sequence(a,b,n):
#     if n==0:
#         return 1
#     c=a+b
#     print(c,end=",")
#     recursive_sequence(c,b+1,n-1)
#
# a=0
# b=1
# n=10   #10 numbers
# recursive_sequence(a,b,n)



#splitting the string in our "k" length
# test_str = 'geeksforgeeksp145'
# k=5
# n=len(test_str)//k
# test=[]
# b=0
# for i in range(0,len(test_str),n):
# 	if len(test_str[i:i+n])==n:
# 		test.append(test_str[i:i+n])
# print(test)   #['gee', 'ksf', 'org', 'eek', 'sp1']



#makes first work as key, and remaining words as value
# test_list = ["gfg is best for geeks", "I love gfg", "CS is best subject"]
# d={}
# for i in test_list:
# 	key,val = i.split(maxsplit=1)   #splits at left side for just once
# 	if val:
# 		d[key]=val
# print(d)    #{'gfg': 'is best for geeks', 'I': 'love gfg', 'CS': 'is best subject'}



#program to create combinations without itertools and using recursion
# def n_length_combo(lst, n):
#     if n == 0:
#         return [[]]
#
#     l = []
#     for i in range(0, len(lst)):   #note - Recursion calls happens inside for loop, so more recursion calls
#
#         m = lst[i]
#         remLst = lst[i + 1:]   #i+1: slicing
#
#         p = n_length_combo(remLst, n - 1)   #returning values from child recurisve functions
#         for i in p:
#             print('list value',n,'----', [m],i)
#             l.append([m] + i)   #adds two lists and then appends into results
#
#
#     return l
#
# #printed values from above, before going to "l.append([m] + i)"
# # list value 1 ---- ['b'] []
# # list value 1 ---- ['c'] []
# # list value 2 ---- ['a'] ['b']
# # list value 2 ---- ['a'] ['c']
# # list value 1 ---- ['c'] []
# # list value 2 ---- ['b'] ['c']
#
# #list value 1 -- returning from child function,  ex: ['b'] []
# #list value 2 -- adds the values "[m]==a" + returning from child function,  ex: ['b'] [] == ['a', 'b']
#
#
# arr = "abc"
# arr=list(arr)
# number_combination=2   #can give upto less than input's length
# print(n_length_combo(arr,number_combination)) #[['a', 'b'], ['a', 'c'], ['b', 'c']]
# #3 combination with 'abcd' - [['a', 'b', 'c'], ['a', 'b', 'd'], ['a', 'c', 'd'], ['b', 'c', 'd']]


#passing input value into raw string
# input = 'the'
# pattern = r'\b{}\b'.format(input)   #passing input value into raw string
# d=re.findall(pattern,'the therausaus')
# print(d)