import pandas as pd
import numpy as np


#Pandas series

#pandas.Series( data, index, dtype, copy)   #series syntax

#index - dictionary key,  data(or)row - dictionary value

# Pandas Series "data,index" values should be list,tuples,numpy_arrays,dictionary

# data=np.arange(5,10)
# s=pd.Series(data)   #using numpy array
# print(s)
# # 0    5     #defaultly index added from '0' to '4'
# # 1    6
# # 2    7
# # 3    8
# # 4    9
#
# data=np.arange(5,10)
# index=[100,101,102,103,104]
# s=pd.Series(data,index)   #index was given
# print(s)
# # 100    5
# # 101    6
# # 102    7
# # 103    8
# # 104    9
#
#
# s=pd.Series({'a':1,'b':2,'c':3,'d':4})    #index - dictionary key,  row(or)data - dictionary value
# print(s)
# # a    1
# # b    2
# # c    3
# # d    4
#
# #like python dictionary, can do all operations, pandas has more separate inbuiltins
# print(s['a'])
# print(s.keys(),s.values)
# print(list(s.items()))
# print(s.pop('b'))



#pandas Dataframe

# pandas.DataFrame( data, index, columns, dtype, copy)   #dataframe syntax - 'columns' additionally added

#data - Row, Columns - column , index - index_number (similar to DB id_number)

# Pandas dataframe "data,index,columns" values should be list,tuples,numpy_arrays,pandas series array, dictionary


# data=pd.Series(np.arange(5,10))    #using pandas series array data
# df = pd.DataFrame(data)
# print (df)
# # 0   6    #similar to Series, Can use it for 1-Dimension data also.
# # 1   7
# # 2   8
# # 3   9
# # 4  10
#
#
#
#
# index=[100,101,102]
# data = [['Alex',10],['Bob',12],['Clarke',13]]
# df = pd.DataFrame(data,index,columns=['Name','Age'])
# print (df)
#        Name  Age
# 100    Alex   10
# 101     Bob   12
# 102  Clarke   13


index=(100,101,102,103)
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}   #column-dictionary key , row - dictinary values
df = pd.DataFrame(data,index)
print(df)
#       Name  Age
# 100    Tom   28
# 101   Jack   34
# 102  Steve   29
# 103  Ricky   42
print(df.columns, df.index,)
print(df['Name'])
print(df['Age'])
print(df.get('Name'))
print(df.keys())
print(df.values)


print(df.shape)   #(4,2)
# print(df.pop('Name'))   #deletes entire column


print(df.head(2))  #prints top two rows
print(df.axes)   #gives index and columns details
print (df.size)  # row*columns -- 4*2 ==8


print(df.sum())
# Name    TomJackSteveRicky
# Age                   133

print(df.mean())   #Age    33.25   #age average value


#descriptive statistics

print(df.describe())   #complete statistics of 'integer column' values data
#              Age
# count   4.000000   #no of occurances
# mean   33.250000   #average value
# std     6.396614   #standard deviation
# min    28.000000   #minimum age value
# 25%    28.750000
# 50%    31.500000
# 75%    36.000000
# max    42.000000   #maximum age value


#deleting,accessing the row values








# s=pd.DataFrame([{'a':1,'b':2,'c':3,'d':4}],index=['sat'])
# print(s)
#      a  b  c  d
# sat  1  2  3  4
