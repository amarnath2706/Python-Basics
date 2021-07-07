#!/usr/bin/env python
# coding: utf-8

# ## Database connectivity and operations using Python.
# For Example, the following is the example of connecting with MySQL database "my_database1" and creating table grades1 and inserting values inside it.

# In[11]:


#import the package
import sqlite3
#connecting with the database
db=sqlite3.connect("mydb1.db")
# Drop table if it already exist using execute() method.
db.execute("drop table if exists grades2")
#create the table as per the requirement
db.execute("create table grades2(id int,name str,score int)")
#Inserting values into the table grades1
db.execute("insert into grades2(id,name,score)values(1,'Jasvee',100)")
db.execute("insert into grades2(id,name,score)values(2,'Amar',90)")
db.execute("insert into grades2(id,name,score)values(3,'Ranju',80)")


# In[12]:


db.commit()


# In[15]:


results=db.execute("select * from grades2 order by id")
for rows in results:
    print(rows)
print('-'*90)


# In[16]:


results = db.execute("select * from grades2 where name='Jasvee'")
for rows in results:
    print(rows)
print('-'*90)


# In[17]:


results=db.execute("select * from grades2 where score>=90")
for grades in results:
    print(grades)
print('-'*90)


# In[19]:


results = db.execute("select name, score from grades2 order by score desc ")
for row in results:
    print(row)
print('-'*90)


# In[20]:


results = db.execute("select name, score from grades2 order by score")
for row in results:
    print(row)
print("-" * 90 )


# In[21]:


results = db.execute("select name, score from grades2 order by score")
for row in results:
    print(row)


# In[ ]:




