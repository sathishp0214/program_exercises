import numpy as np

a=np.array([1,2,3,4])    #defaultly "int32" dtype numpy array

arr1 = np.array([11,-2,23.3,4,75],dtype=np.int64)   #defines int64 dtype numpy array

x = np.array([1,2,3,4,5], dtype = np.int8)
print (x.itemsize)   #prints 1   #prints byte size of only one element of array
#similarly for int16 - 2 bytes, int32 - 4 bytes, int64 - 8 bytes.



# s=np.array(['a','b','c'])  #creating string numpy array


# a=np.zeros((3,2),dtype=float)  #creates float type zeros in 3X2
# print(a)
#similarly we can do np.ones()  #one values instead of zeros



# a=np.array([1,2,3])    #single dimensional array
#
# a=np.array([(1,2,3),(4,5,6)])   # 2 dimensional array
#
#
#
# print("rrr",a.ndim)    #2 - prints number of dimensional array




# x = np.arange(10,20,2)   #similar to range()
# print (x)

# x = np.linspace(10,20,5)   #mostly used in for loop
# print (x)    #[10.  12.5 15.  17.5 20. ]   #linspace -- prints the evenly spaced number accurately in float numbers
#
# x = np.linspace(1,2,20)
# print (x)   #[1.         1.05263158 1.10526316 1.15789474  prints so on
#
# a = np.logspace(1.0, 3.0, num = 15)   #num=15 , it will print evenly spaced 15 numbers, between 1.0 and 3.0 log scale numbers
# print (a)
#
# a = np.logspace(1,10,num = 10, base = 2)
# print (a)  #[   2.    4.    8.   16.   32.   64.  128.  256.  512. 1024.]   #prints base 2 , 2 pow 1, 2 pow 2 etc



#
# a = np.array([(1,2,3,4,5,6),(1,2,3,4,5,6),(1,2,3,4,5,6)])
#
# print(a.size)   #18 - total elements
#
# print(a.shape)   #(3, 6)  - 3 - rows, 6 - columns



#Reshape - changes the row and columns dimensionals, changes 1D to 2D, 2D to 3D etc

# d=np.arange(3).reshape(3,1)   # 3-rows,1-columns
# print(d)
#
# [[0]
#  [1]
#  [2]]


# a=a.reshape(6,3)  #changes the above array into 6 rows and 3 columns - size of above array is 18, so 6X3=18

# [[1 2 3]
#  [4 5 6]
#  [1 2 3]
#  [4 5 6]
#  [1 2 3]
#  [4 5 6]]


# a=a.reshape(9,2)   #similarly 9 rows and 2 columns
#
# a=a.reshape(3,3,2)   #3- array divisons, 3-rows , 2-columns 3X3X2=18 -- creates 3 dimensional array
# print(a,)

# [[[1 2]
#   [3 4]
#   [5 6]]
#
#  [[1 2]
#   [3 4]
#   [5 6]]
#
#  [[1 2]
#   [3 4]
#   [5 6]]]

# array = np.arange(24).reshape(2,2,2,3)   #4-D dimensional array, (2 X 2=array division) , 2-rows, 3- columns
# print("\nOriginal array reshaped to 4D : \n", array,np.ndim(array))
#
# array = np.arange(48).reshape(3,4,2,2)   #4-D dimensional array, (3 X 4=array division) , 2-rows, 2- columns
# print("\nOriginal array reshaped to 4D : \n", array,np.ndim(array))
#
# array = np.arange(24).reshape(2,6,2)   #3-D dimension, 2- array division segment, 6-rows and 2-columns
#
# print(array,np.ndim(array))


#indexing in numpy
# a=np.array([(1,2,3,4),(3,4,5,6)])
# print(a[0,3])  # prints 4   ## similar to list indexing is -- a[0][3]


#slicing in numpy

# a = np.array([[1,2,3],[3,4,5],[4,5,6]])
# print(a[1:])   #[[3 4 5] [4 5 6]]    #for single dimensions, works normally as python slicing

# x = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]])
# print (x[1:4,1:3])   #1:4 - rows index level, prints from 1st index,
# #1:3 - column index level, from 1st row index, all columns from 1st index
# [[ 4  5]
#  [ 7  8]
#  [10 11]]






#for loop iterating

# for i in np.arange(10,20):
#     print(i)
#
# x = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]])
# y = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]])
#
#
# for i in np.nditer(x):
#    print (i)   #prints x values one by one
#
# for i,j in np.nditer([x,y]):
#    print (i,j)   # prints x and y (0,0) values



#addition, substraction, multiplication, division of arrays (sizes of all array should be same)
x= np.array([(1,2,3),(3,4,5)])
y= np.array([(1,2,3),(3,4,5)])
# z= np.array([(1,2,3),(3,4,5)])
#
# print(x+y)    #[[ 2  4  6] [ 6  8 10]]
#
# print(x-y)
#
# print(x*y)    #[[ 1  4  9] [ 9 16 25]]
#
# print(x/y/z)   #using three arrays, [[1.         0.5        0.33333333] [0.33333333 0.25       0.2       ]]



# sum(), min() , max(), sort(), unique()  with axis 0 and 1

# axis=0 means columns, axis=1 means rows
# a= np.array([(1,2,3),(3,4,5),(0,2,5)])
#
# print(a.sum(axis=0))    #[4 8 13] - 1+3+0=4, 2+4+2=8 and 3+5+5=13
#
# print(a.sum(axis=1))     # [6 12 7]  - 1+2+3 = 6 , 3+4+5 = 12, 0+2+5=7
#
# print(a.min(axis=0))
# # [0 2 3]  -minimum values of all columns ,0 value is minimum value in 0th index,2 value is minimum value in 1th index,3 value is minimum value in 2th index
#
# print(a.min(axis=1))
#[1 3 0] - 1 - minimum of (1,2,3) , 3 - minimum of (3,4,5) , 0 - minimum of (0,2,5)


# print (np.sort(a,axis=0))

# [[0 2 3]
#  [1 2 5]
#  [3 4 5]]






# x= np.array([(1,2,3),(3,4,5),(8,9,67)])
# print(x.ravel())    #[ 1  2  3  3  4  5  8  9 67]   #converts multi-dimensional array into single array

# a = np.array([10,100,1000])
# b = np.array([1,2,3])
# print(np.power(a,b))    # a power b ---> [        10      10000 1000000000]


# a = np.array([[10,20,30],[40,50,60],[70,80,90],[100,110,120]])
#
# print(np.average(a))  ##prints 65, np.mean() = np.average() (summing the numbers and divide)



# x=np.array([[1,2],[3,4]])
# y=np.array([[12,30]])
# print(np.concatenate((x,y)))
#[[ 1  2]
 # [ 3  4]
 # [12 30]]



# a=np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
# b=np.array([[11, 21, 31], [42, 52, 62], [73, 83, 93]])

# print(np.append(a,b))   #[10 20 30 40 50 60 70 80 90 11 21 31 42 52 62 73 83 93]

# c=np.append(a,b,axis=0)   #append function with column axis
# print(c)
# [[10 20 30]
#  [40 50 60]
#  [70 80 90]
#  [11 21 31]
#  [42 52 62]
#  [73 83 93]]


# x= np.array([(1,2,3),(3,4,5)])
# y= np.array([(6,7,8),(9,10,11)])
#
# print(np.vstack((x,y)))   #vertical stack
# # [[ 1  2  3]
# #  [ 3  4  5]
# #  [ 6  7  8]
# #  [ 9 10 11]]    #appending arrays in vertically
#
# print(np.hstack((x,y)))   #horizontal stack
# [[ 1  2  3  6  7  8]
#  [ 3  4  5  9 10 11]]   #extending arrays with same index, 0th index of one array added with 0th index of another array





# x = np.array([1.48,1.41,0.0,0.1])
# print (x.argsort())  # [2 3 1 0]  - prints sorted value's index in same order


#using conditions for filtering values

# x = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]])
# print (x[x>5])   #using conditions,  #[ 6  7  8  9 10 11]
#
# print (x[x!=3])   #[ 0  1  2  4  5  6  7  8  9 10 11]

# a = np.array([1, 2+6j, 5, 3.5+5j])
# print (a[np.iscomplex(a)])   #filtering complex values only   #[2. +6.j 3.5+5.j]
#
# a=np.arange(12)
# b=np.where(a<6,a,5*a)    # 5*a is default value for 'False' conditions, so values lesser than '6' is True cases.
# print(b)   # [ 0  1  2  3  4  5 30 35 40 45 50 55]


#converts python list of numbers (or) strings (or) tuple into numpy array

# x = [(1,2,3),(4,5,6),(7,8,9)]
# x=['apple', 'banana', 'cherry','10','30.5']
# a = np.asarray(x)    #converts python list (or) tuple into numpy array
# print (a,a.dtype)

#converts string of numbers into numpy array as 'integer or float type'
# x=['1','2','3','4']
# a=np.array(x,dtype='i')   #converts into integer
# a=np.array(x,dtype='f')   #converts into float
# print(a,a.dtype)


#converts numpy array into python list of numbers (or) strings
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# arr=np.array(['apple', 'banana', 'cherry','10','30.5'])
# list1 = arr.tolist()    #converts numpy array into python list
# print(list1,type(list1))

# arr1=np.array(['geeks', 'for', 'geeks'])
# print(arr1,arr1.dtype)
# d=arr1.tobytes()
# print(str(d))



#converts a string into numpy array

# b='Man is good boy'
# a=np.char.split(b,sep=" ")
# print(a,a.dtype,type(a))
#
# b='Man is good boy'
# a=b.split()  #normally changes a string into list
# arr=np.asarray(a)
# print(arr,arr.dtype,type(a))





