#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Getting Started with Pandas:
import pandas as pd
from pandas import Series, DataFrame


# In[2]:


#To get started with pandas you need to get started with pandas two set of data structure and they are series and dataframe. 


# In[3]:


#Series


# In[8]:


#Series is like an one dimensional array, which has elements that are of same type and each value is indexed. 
#throughout this series we are going keep the names of the given variables in numerical ordering since we are going to deal with the same variables multiple times.
series1=pd.Series([1,2,3,4])#Creating a Series
series1
#In the result the right side is index and values are assigned to corresponding index.


# In[9]:


#Want arrays in pandas as numpys you can use the following command.
series1.array


# In[12]:


series1.index#Know the index using this method


# In[13]:


#How to specify index in pandas
series2=pd.Series([3,4,5,6],index=["a","c","d","b"])
series2


# In[14]:


#To take out values from a specified index, we can use the function as
series2["d"]


# In[16]:


#To access multiple elements in the series using index we can us the command
series2[["a","d","b"]]


# In[20]:


#Doing mathematical operations or using boolean operation will not affect the index it will only change the corresponfing values
#for example
series2[series2>0]
#Since everyelement is greater than zero it will print all but no affect is on the function.


# In[21]:


series2*2


# In[ ]:


#Another way to think of a series is a fixed length dictionary. 
#It is sued in may cases where dictionary is used.


# In[22]:


"b" in series2


# In[23]:


"f" in series2


# In[25]:


#You can create a series from a fictionary. Where the key is used as an index and values is used as values
dict1={"Jan": 200,"Feb":300,"Mar":400,"Apr":500,"May":600,"June":700,"July":800}
series3=pd.Series(dict1)
series3


# In[2]:


#A series can be converted back to dictionary using to_dict
series3.to_dict()


# In[ ]:


#If you want to modify the dictionary keys, you can modify this by using the pandas 
months=["Feb","Jan","Mar","May","Apr","June","July","Kali"]
series4=pd.Series(dict1, index=months)
series4
#If coressponding value to a key is not present in the dictionary than Nan value is present which is called as integer.


# In[5]:


import pandas as pd
import numpy as np
series5=pd.Series([1,2,3,4,5],["a","b","c","d","e"])
#Non Avilability of the values in the given dictionary
pd.isna(series5) # When you generate output to check wether elements are present in the given series or not.
#Here all results are false beacuse there is no null values in the series


# In[6]:


#Avilability of the elements can be checked be in the series as follows
pd.notna(series5)


# In[ ]:


#The case of missing data will be further checked in the comming sections.


# In[9]:


#You can name the series, and name the index
series5.name="Price "#Name the series
series5.index.name="months"#Name the index
series5


# In[10]:


#Data frame:A dara frame represnts a rectangular table of data and contains an ordered, 
#named collection of columns, each of which can be a different value type(numeric,string, Boolean etc.)


# In[16]:


#I think you all have made tables, and this is just like filling series. Dataframe is basically used to deal with datas that have myltiple rows and columns
data1={"students": ["Elon","Jeff","Bill","Sam"],#Remember this comma
        "marks": ["96","91","96","94"],#The marks are random no offence😂
        "rank": [1,3,1,2]
    }
frame1=pd.DataFrame(data1)
frame1
    


# In[ ]:


#You can create any numbers of rows and columns and can fill the data using data frame


# In[17]:


#Selecting the first five rows:
frame1.head()# this command selects the first five rows in the data. Primarily used in large datasets


# In[18]:


frame1.tail()#Returns the last five rows


# In[27]:


#Want to change the order of columns in the given data frame use this
frame2=pd.DataFrame(data1, columns=["marks","rank","students"])
frame2


# In[28]:


#You can add a column, if the value is not present in the given column than na is the ouput in the given table
frame2=pd.DataFrame(data1, columns=["marks","rank","students","percentage"])
frame2


# In[ ]:


#See than the percentage gives the value of NaN


# In[29]:


#A column in the data frame can be retrieved by calling it. 
frame2["students"]


# In[31]:


#You can also use the dot attribute do this task.
frame2.marks


# In[ ]:


#It's better to use the previous method beacuse in dot method, if the name of column is something that conflicts witht the object in the python that this process will not work. White spaces and special symbols will also not work.


# In[ ]:


#Just like we retrieved columns we can also retrieve rows. 
#iloc or loc command cab used to do this. 


# In[33]:


frame2.loc[1]


# In[34]:


frame2.iloc[2]


# In[36]:


#Want to fill the empty column.#percentage
frame2["percentage"]=90
frame2


# In[43]:


#Want to add ranges in the percentage section
frame2["percentage"]=np.arange(4)
frame2


# In[44]:


#You want add your own values in the percentage section than what do you do?
#first assign the values by creating a series. Than you can further work on the problem
val=pd.Series([100,99,100,99.8])
frame2["percentage"]=val
frame2
#This is simple ways of updating the values in the given column in the given data frame


# In[57]:


#Lets learn how to delete columns. This can be simply done by delete commands on python.
#first lets create an empty column.
frame2["Deleting Practice"]=0
frame2


# In[59]:


del frame2["Deleting Practice"]
frame2
#here is how the specified columns are deleted.


# In[62]:


#to check the columns in the data frame
frame2.columns
#when we are viewing the data here we are actually viewing the original column and not a copy of it.


# In[63]:


#to copy the columns you can use .copy() for example
columnscopy1=frame2.columns.copy()
columnscopy1


# In[67]:


#Suplying nested dictionaries in the pandas.
#A nested dictionary is a dictionary inside a dictionary.
billionranks={"student":{1:"Elon",2:"Jeff",3:"Bill",4:"Sam"},"marks":{1:96,2:91,3:96,4:94}, "rank":{1:1,2:3,3:1,4:2},"percentage":{1:100,2:99,3:100,4:99.8}}
frame3=pd.DataFrame(billionranks)
frame3


# In[ ]:


#Evaluate the result, the outer is key is considered as column and further key is considered as index.


# In[68]:


#want to transpose a frame. You can transpose the same way you did with numpy arrays.
frame3.T


# In[72]:


#As we have seen that the inner keys are specified as index in the pandas but this will not hold true if we supply a seperate index.
#for example
pd.DataFrame(billionranks,index=[1,2,"c","d"])


# In[ ]:


#Those values are not kept in the index are not mentioned here. This an effective way of accessing dictionaries using pandas


# In[73]:


#What is the types of possible data inputs than can be put in the data frame constructor.
#2D ndarray: a matrix of data, passing optional row or column labels.
#dictionary of arrays, list or tuples: Each sequence becomes a column and every sequence should have the same length
#numpy structured/record array: treated as dictionary of arrays.
#dictionary of series: each value becomes a column, indexes from each series are unioned together to form the result's row index if no explicit index is passed
#dictionary of dictionaries: each inner dictionary beomes a a column; keys are unioned to form the row index as in the "dictionary of series", case.
#list of dictionaries or Series:: Each item becomes a row and key or series index becomes the name of the columns
#List or list or tuples: treated as the "2D ndarray"
#another data frame: the data frame's indexes are used unless differet ones are passed
#numpy masked array: like the 2D ndarray.


# In[77]:


#you can also name the columns and row by supplying the commands as :
frame3.index.name="S.N"
frame3.columns.name="Table"
frame3


# In[78]:


#Convert data frame into a numpy array you can use the following command
frame3.to_numpy()


# In[8]:


import pandas as pd
import numpy as np
#Index Objects
#pandas index objets are responsible for holding the axis labels( including a DataFrame Column Names) and other metadata(like the axis name or names). 
#Any array or other squence of labels you use when constructing Series por DataFrame is internally converted to an index
obj1=pd.Series(np.arange(3),index=["a","b","c"])
index1=obj1.index
index1
index1[1:]#remember that the slicing is done on the basis of the stop start method, first stop says that stop removing the elements and second start says start removing the elements.


# In[10]:


#index objects are immutable and cannot be modified by the user.
#this feature of an index being immutable, helps to share the index across the data structure
obj2=pd.Index(np.arange(3))
index2=obj2
obj3=pd.Series([1,2,3],index=obj2)
obj3


# In[11]:


#Study of an index is sometimes neglected yet it is useful to study them sometimes
#We have the studied the array like property of an index
#It is worth to note also the set type properties of an index.
-21 in obj3.index
#can be also used in data frames .


# In[ ]:


#Some properties of index that are worth noting are as follows:
#Append() this helps to put the elements in the list
#difference() intersction() and union() can be also used in the similar way as it is used in the set
#delete(): Computes new index with element at index i deleted
#drop(): Compute new index by deleting passed values
#insert(): Computes new index by insertng element at index i 
#is_monotonic: Computes and gives Boolean Expression for wether each element is greater than or equal to the previous element.
#is_unique: Returns True if the index has no duplicate values.
#unique(): Compute te array of unique values in the index.


# In[ ]:


#This introductory panda lesson will help you move ahead in data manupulation using pandas data frame and series.


# In[ ]:


#Regards
#Ankit Sangroula
#@mechengics


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




