#!/usr/bin/env python
# coding: utf-8

# ## Strings

# In[1]:


j='Jasvee'
print(j)


# In[2]:


type(j)


# In[4]:


# Difference between print function and without using print function
#print(j) and j


# In[5]:


#if you just type the variable name j and excuted that then you can able to see the output single quotes
j


# In[6]:


#If you run the or excute the string variable using print function then it will execute without quotes
print(j)


# ## Indexing and Slicing
# ##### *To grab only single element or item from the string or string variable is called indexing.
# ##### *To grab more than one items or elements from the string variable and also from one position to specific index position also we can grab      those items are called slicing.

# In[7]:


print(j)


# ### Indexing

# In[8]:


#Indexing
j[0]


# In[9]:


j[2]


# In[13]:


j[5]


# In[14]:


# We got an error as index out of range because no such index position available in string
j[6]


# In[19]:


# Negative indexing
#  J  a  s  v  e  e 
# -6 -5 -4 -3 -2 -1
j[-1]


# In[21]:


j[-2]


# In[22]:


j[-4]


# In[23]:


j[-6]


# ### Slicing

# In[15]:


#From 0 to 2 index
j[0:3]


# In[16]:


#From 0 to all
j[0:]


# In[17]:


#From 0 to 3
j[:4]


# In[18]:


# All index
j[:]


# In[27]:


# Slicing using negative index
#  J  a  s  v  e  e 
# -6 -5 -4 -3 -2 -1
# Starting from -5 index to -2 index and excluding the -2 index
j[-5:-2]


# In[28]:


j[:-1]


# In[30]:


j[3:-1]


# In[31]:


#Slicing using step index
#[start position:end position:stepindex]
j[0:5:2]


# In[33]:


j[-6:-2:2]


# In[34]:


#Reverse the string
j[::-1]


# In[35]:


# Stirng properties
# Now let's i'm gonna to do reassignment using indexing and slicing. Strings are immutable you can't modify the values
j[0]='A'


# In[36]:


j[0:3]='A'


# In[37]:


#Concatenation
j + 'Adithri' + "." + 'Amarnath'


# In[47]:


#Print formatting with \n -- new line
a='Adithri'
b='Father name : '
c='Amarnath'
d="Mother name : "
e='Ranjani'
print("{} {}'s \n{} {}, \n{} {}.".format(j,a,b,c,d,e))


# In[51]:


# String Repetition using *
print(j*20)


# ## String methods (or) Functions

# In[52]:


# 1. Type function
type(j)


# In[53]:


#2.Id function
id(j)


# In[54]:


#3.Len function - It returns the no of items( total no of length) or characters in the variable
len(j)


# In[56]:


#4.Count function - It returs the no of occurence of the particular value in the variable
j.count('e')


# In[57]:


#5.Upper function
j.upper()


# In[58]:


#6.Lower function
j.lower()


# In[59]:


#7.Find function - It find and returns the index position of the first occurence of the value
j.find('e')


# In[60]:


#8.Replace - It takes 2 arguments: 1st argument old value, 2nd argument new value to be replace
j.replace('a','A')


# In[61]:


#9.Split function - Split by a specific element (doesn't include the element that was split on)
j.split('v')


# In[62]:


#Split a string by blank space (this is the default)
a="Adithri belongs to Thuraiyur"
a.split()


# In[64]:


#10.Center function - This method allows you to place your string 'centered' between a provided string with a certain length.
j.center(20,'*')


# In[65]:


#11.Expandtabs function - will expand tab notations \t into spaces 
# .expandtabs(tab size)
'hello\thi'.expandtabs()


# In[73]:


'hello\tJasvee\tAdithri'.expandtabs(40)


# In[74]:


# Check methods
#12.isalnum()- It checks whether if all characters in string are alphanumeric and it returns bool result. 
j.isalnum()


# In[81]:


#Here * is not an alphanumeric one
t='234***'
t.isalnum()


# In[78]:


s="20Jasvee"
s.isalnum()


# In[83]:


#13.isalpha- checks whether the variable in the content having all the characters are in alphabets or not
t.isalpha()


# In[84]:


s.isalpha()


# In[85]:


j.isalpha()


# In[86]:


#14.Islower- checks whether all the characters are in lower case
j.islower()


# In[87]:


#15.Isupper - checks whether all the characters are in upper case
j.isupper()


# In[88]:


z='JASVEE'
z.isupper()


# In[89]:


#16.isspace- return "True" if all characters in S are whitespace.
j.isspace()


# In[90]:


w='Amar Jasvee Ranju'
w.isspace()


# In[93]:


y=' '
y.isspace()


# In[94]:


#17.istitle()- It checks whether the starting letter is in uppercase or not.
z.istitle()


# In[95]:


j.istitle()


# In[96]:


#18.endswith()-it checks whether the variable ends with specific given character.
j.endswith('r')


# In[97]:


j.endswith('e')


# In[99]:


#19.Partition- It is used to return a tuple that includes the separator (the first occurrence), the first half and the end half.
j.partition('e')


# In[100]:


j.split('e')


# ### Here are the difference between split and partition function: 
# ##### split fn --  will split on the basis of character which u passed and it will exclude that element too and finally it will gives u the result in the form of list --- j.split('e') ----> ['Jasv', '', '']
# ##### partition fn -- same as split but it has two changes. 1. it will not exclude the element based on which you try to partition, 2. it will gives the output in the form of tuple --- j.partition('e') ---> ('Jasv', 'e', 'e')
# 

# In[ ]:




