#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('Jasvee)


# In[2]:


7/0


# In[3]:


#here it will terminate the program and will not allow me to execute to further process and will come out of the loop without executing the remaining part of the program.
#In a industry standard of code will always try to create the code will handle the exception and also will allow to execute further other set of codes.Even if there is a error


# In[4]:


#Best example --search exception handling in wikipedia
#Exception handling is one of the most important concept whle we create a code so you are supposed to handle exception if you are not supposed to handle exception then it will become a disaster.
try:
    f=open('jk.txt','w')
    f.write('Write this line in to jk.txt')
except IOError:
    #This only check for an IOError exception and then execute this print statement
    #Except block will come immeadiately after the try block.
    print("Error:Couldn't find the file")
else:
    print("Content written successfully")
    f.close()
#try is a block where you can keep all suspicious code which menas if i have some doubt with the code. so we used to keep all of those codes inside a block called as try.
#If ur code is gng to crash inside the block whatever you written inside in the try block basically it will not terminate your program.it will come inside the except block.
#Here the else part will work after the try block will executed it successfully.


# In[8]:


#Execute with read mode
#here we have a problem gng to face because in 1st line we are going to read the content and in the next line we r performing the write operation.
#It will not execute the next set of codings too.and it will stop the execution 
try:
    f=open('jk.txt','r')
    f.write('Write this line in to jk.txt')
    print("Jasvee")
except IOError:
    #This only check for an IOError exception and then execute this print statement
    print("Error:Couldn't find the file")
else:
    print("Content written successfully")
    f.close()


# In[7]:


#Exact error your going to get an error:
f=open('jk.txt','r')
f.write('Write this line in to jk.txt')


# In[16]:


# Suppose i dont have an idea about hat kind of an error i'm supposed to face then leave just except block then leave it
# we can create mor no of try except block
try:
    f=open('hjk.txt','r')
    f.write('Success')
except Exception as e:
    print("Sorry i'm unable to find the file")
else:
    print('Completed')
try:
    print(5/0)
except:
    print('not a valid')
print("Jasvee Adithri")


# ### Finally

# In[12]:


# Whenever you want to open a file and it should close the file even if there is an exception while reading or writting the data.
# Suppose if i'm doing the connectivity to the databases and due to some issue then it will thrown an exception but it still supposed to close my db connectivity.
# Basically i have some code which i have to execute at any cost. So in that case i can try to put that set of codes inside a block called as finally.
# If you are keep that particular block of codes in to a finally block.Finally is a kind of block which will execute itself for sure.
try:
    f=open('hjk.txt','r')
    f.write('Success')
finally:
    print("Always execute finally block of codes")
#here the finally block will execute even if we are failed to implement the except block although i'm get an error.  


# In[13]:


#Else and Finally 
#else will execute only if try block will execute successfully
#Finally block will execute suppose if u got an error or without error in try block then forsure it will excute the finally block. 


# In[18]:


dir(Exception)


# In[31]:


def askint():
    try:
        user_input=int(input('Enter the integer'))
    except: 
        print("Looks like which u have entered is not an integer")
    finally:
        print(" i'm executed it")
    print(user_input)

        


# In[33]:


askint()


# In[34]:


def askint():
    try:
        user_input=int(input('Enter the integer'))
    except: 
        print("Looks like which u have entered is not an integer")
        user_input=int(input("Try again pls enter an integer!"))
    finally:
        print(" i'm executed it")
    print(user_input)
askint()


# In[38]:


#how to check continously
def askint():
    try:
        user_input=int(input('Enter the integer'))
    except: 
        print("Looks like which u have entered is not an integer")
        try:
            user_input=int(input("Try again pls enter an integer!"))
        except:
            print("again not an integer, pls retry")
    finally:
        print(" i'm executed it")
    try:
        print(user_input)
    except:
        print("not a valid input")


# In[39]:


askint()


# In[40]:


#Using while, break, continue, try, except, finally , else
def askint1():
    #Universal condition
    while True:
        try:
            val = int(input("Please enter an integer: "))
        #If i made a mistake it comes to except block    
        except:
            print("Looks like you did not enter an integer!")
            #Here continue it will again go to the loop (try block)
            continue
        #If you found out the entered input is an integer then i need to execute the else block
        else:
            print('Yep thats an integer!')
            #Then i vl break this loop
            break
        #In every iteration it will execute the finally block
        finally:
            print("Finally, I executed!")
        print(val) 


# In[41]:


askint1()


# In[ ]:




