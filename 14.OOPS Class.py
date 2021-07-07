#!/usr/bin/env python
# coding: utf-8

# ## Object Oriented Programming
# (OOP) is a programming paradigm that allows abstraction through the concept of interacting entities. This programming works contradictory to conventional model and is procedural, in which programs are organized as a sequence of commands or statements to perform.
# 
# We can think an object as an entity that resides in memory, has a state and it's able to perform some actions.
# 
# More formally objects are entities that represent instances of a general abstract concept called class. In Python, "attributes" are the variables defining an object state and the possible actions are called "methods".

# ## Class
# * Class is a real world object example: car 
# * The real world object have some properties and methods
# * Python support scripting as well as OOP's concept
# * For exmaple consider there is a car. if i say car and you don't have idea about which car i'am talking about eg: Audi or Bmw.
# * Class is a blue print of the real world object 
# * Class is a classification or seperation of real world entity.
# * Object is a variable or instance of a class which means variable of a particular class is called object
# * int,string,float,bool - primitive class
# * List,set,tuple,dictionary - collection class

# In[1]:


#To create a class
class test():
    #body of the class- to specify what it should do


# In[2]:


# pass keyword - Pass keyword only available in python and used to skip the body part and u r not supposed to write the body part.
class test1():
    pass


# In[7]:


class Person:
    pass
# i'm gng to create an object of the person class below
P=Person()
# Here P is the variable of the class Person
#Whatever property inside the class(Person) we will be able to access those properties or attributes
#But as of now here i don't have any properties and now i'm going to create an attributes.
P.name="Jasvee"
P.surname="JA"
P.dob="20/09/2018"
# Here name,surname,dob(Properties) is a kind of variable which i have created for a particular class through an Person class object
# And also i'm trying to pass the value of the particular attribute to the class.
# Whatever you supposed to access the properties inside the class. you vl be able to do that with the help of an object
# outside of the class u vl not be able to access
#Here P is the object of the Person class and its print only the object location of the Person class
print(P)

#Here i'm accessing the attribute of the Person class with the help of an object
print("{} alias {} was born on {}".format(P.name,P.surname,P.dob))

#The above is not a standard way and it is a bad practice i would say
#Note - in one class i vl be able to create an infinite no of object for particular class
PA = Person()
PA.name='Amar'
PA.surname='ARJ'
print(PA.name)


# In[8]:


#What is a good practice, 
#How vl be able to create a class in a actual way/how vl be to pass the data/how vl be to create an object.
#A. Create a class
class Person:
    #2. I'm trying to use methods
    #3.i'm using __init__ -- This is the initialization method and this is the default method that u vl be able to find out in a class.
    #4.__init__ does? -- Basically whenever u vl be able to find some method __xxx__ means this is the inbuilt method and try to override this method.
    #5. self --Whenever we r gng to create a method within a class, we created a 1st variable called 'Self'.
    #6. Here the 'self' variable behaves like a pointer not a keyword. which denotes it points to a class called "Person".
    #7. Now what the pointer does? Here i'm trying to initialize the value(variables --> name,surname & dob) to the class.
    #8. So we have 3 variables that i'm gng to pass at a run time at the time of creation of an object.
    #9. Class should take all of those variables and it should be able to return all of those variables with respect to that object at any point of a time.
    #10. It is some what equvalant to contructor but constructor is not avilable in python but in Java or C it is available.
#B.Method to initialize values to the class
#3variables - name,surname,dob
    def __init__(self,name,surname,dob):
        # Passing values of the corresponding varibles to the class Person   
        #Self is like a kind of mapping
        #Self.name -- self.name = name(whatever name you have written over here it will try to provide the name to person class)
        #self.name variable belongs to the class
        #name -- is an object which you are going to get from the  object
        self.name1 = name
        #Self.surname -- self.surname = surname(whatever surname you have written over here it will try to provide the name to person class)
        self.surname = surname
        #Self.dob -- self.dob = dob(whatever dob you have written over here it will try to provide the name to person class)
        self.dob = dob 
        
        #Person Class Variables are = self.name,self.surname,self.dob
        # Object (method variables) variables are - name,surname,dob
        
#C.After creation of class what i'm trying to do is i'm trying to create a variable of the class called as an object.
P=Person("Jasvee",'Adithri Amarnath','20/09/2018')
#Here it's printing just the memory location of the object of the Person class
print(P)
print("Ms.{} alias {} was born on {}".format(P.name1,P.surname,P.dob))


# In[9]:


class car:
    #Self(pointer) instead of self you should give any values like xyz and you are not supposed to give self everytime, but in many cases u vl be able to find self
    def __init__(xyz,model,body,mileage):
        xyz.model1=model
        xyz.body1=body
        xyz.mileage1=mileage
#Here i have created two variable like Tata and Ford for the car class 
Tata=car("TATA ALTROZ",'Alpha model','23Kmpl')
Ford=car("Ford Free style",'Normal','21kmpl')
print("Car model : {}, Engine model : {}, Mileage : {}".format(Tata.model1,Tata.body1,Tata.mileage1))
print("Car model : {}, Engine model : {}, Mileage : {}".format(Ford.model1,Ford.body1,Ford.mileage1))
type(Tata)
id(Tata)


# In[10]:


#Overloading - Generally same function name with diff arguments
#Overloading is applicable in python but its takes the latest __init__ method not every method

class Jasvee:
    #Method 1
    def __init__(self,name,fname,mname):
        self.Name=name
        self.Fname=fname
        self.Mname=mname

    #Method 2
    def __init__(self,age,dob,gender,city):
        self.Age=age
        self.Dob=dob
        self.Gender=gender
        self.City=city
#For sure v vl be get an error like below
JA=Jasvee('Adithri','Amarnath','Ranjani')
print(JA.Name,JA.Fname,JA.Mname)


# In[27]:



#Overloading - Generally same function name with diff arguments
#Overloading is applicable in python but its takes the latest __init__ method inside the class not every method

class Jasvee:
    #Method 1
    def __init__(self,name,fname,mname):
        self.Name=name
        self.Fname=fname
        self.Mname=mname

    #Method 2
    def __init__(self,age,dob,gender,city):
        self.Age=age
        self.Dob=dob
        self.Gender=gender
        self.City=city

JA=Jasvee(1,2018,'Female','Thuraiyur')
print(JA.Age,JA.Dob,JA.Gender,JA.City)


# In[15]:


#__str method__

class Jasvee:
    def __init__(self,name,age,yearofb):
        self.Name=name
        self.Age=age
        self.Yearofb=yearofb
#Here i'm using age method and in this i'm passing my own varaible- currentyr
#And then own variable - class variable from Jasvee class
#If i'm trying to invoke some of the class variable for sure i have to use self keyword or some other pointer name.
#If am not using self keyword then i will not be able to invoke a class variable.
#So with in a class you have to access something so you will have to use a  self name for pointer.
#Outside of the class if you want to access then we need to use object name.
def age(self,currentyr):
        return currentyr-self.Yearofb
#If u print the command instead of showing the output values it show only the memory address of the location. to solve this we need to cerate the seperate str method to display the output.  
# Here __str__ is an inbuilt method 
    def __str__(self):
        return "{} {} was born in ".format(self.Name,self.Age,self.Yearofb)
    
J=Jasvee("JasveeAdithri",'Amar',2018)
print(J)
#calling age method with the help of class Jasvee object  
print(J.age(2020))


# In[22]:



#__dict__ is a special attribute is a dictionary containing each attribute of an object.
# We can see that prepending two underscores every key has _ClassName__ prepended.

class Jasvee:
    def __init__(self,name,age,yearofb):
        self.Name=name
        self.Age=age
        self.Year=yearofb
    def age(self,currentyr):
        return currentyr-self.Yearofb
    #If u use the print function,instead of showing the output values it show only the memory address of the location. to solve this we need to cerate the seperate str method to display the output.  
    def __str__(self):
        return "{} {} was born in {} ".format(self.Name,self.Age,self.Year)
    
J=Jasvee("JasveeAdithri",'Amar',2018)
print(J)
print(J.__dict__.keys())


# ## Protect your abstraction
# Here the instance attributes shouldn't be accessible by the end user of an object as they are powerful mean of abstraction they should not reveal the internal implementation detail. In Python, there is no specific strict mechanism to protect object attributes but the official guidelines suggest that a variable that has an underscore prefix should be treated as 'Private'.
# 
# Moreover prepending two underscores to a variable name makes the interpreter mangle a little the variable name.

# ### Abstraction :
# You might heard about public,public protected,private in other pgmg languages.
# If a class or variable or method is public so in that case you will be able to access those entities within a class outside of the class, within a package or outside of the package and in some other classes (Full access)
# 
# If it is protected you will be able to access something within a class, outside of the class but outside of the package you will not be able to access.
# 
# If it is private you will be able to access just within a class , outside of the class you will not be able to access and 
# outside of the package you will not be able to access.
# 
# So this is called as Abstraction. Abstraction is basically a oops programming language. In Python it's bit weird and it doesn't exixts in python but it exist's in some other form.

# In[48]:


class Amar:
    def __init__(self,name,age,dob):
        #_name,_age,_dob variable name it means that i'm trying to create variables for Person class and all this variables are protected variables.
        #So it doesn't  mean that it is protected variable no, you will be able to access anywhere and outside of the package even. It just a notation inside the python
        #There is no strict provision which can define that if it is protected so u will not be able to access beyond this limit.
        #It simply means that whenever i'm gng to use this variable i'm assume that you are mature enough person or programmer who will try to handle this things by clear.
        #So it just a notation in Python not a provision.
    
        self._name=name
        self._age=age
        self._dob=dob
    def __str__(self):
        return "{} was born in {} and now she is {} years old".format(A._name,A._dob,A._age)
A=Amar('Jasvee',20,2018)
A._name
#print("{} was born in {} and now she is {} years old".format(A._name,A._dob,A._age))
print(A.__dict__.keys())
print(A)


# In[39]:


#Private variable
class Mar:
    def __init__(self,name,age,dob):
        #_name,_age,_dob variable name it means that i'm trying to create variables for Person class and all this variables are protected variables.
        #So it doesn't  mean that it is protected variable no, you will be able to access anywhere and outside of the package even. It just a notation inside the python
        #There is no strict provision which can define that if it is protected so u will not be able to access beyond this limit.
        #It simply means that whenever i'm gng to use this variable i'm assume that you are mature enough person or programmer who will try to handle this things by clear.
        #So it just a notation in Python not a provision.
    
        self.__name=name
        self.__age=age
        self.__dob=dob
M=Mar('Jasvee',20,2018)
#M.__name

#Why error because it is a private variable and whenever you try to create an protected variable internally your class is trying to giva a notation.
#what kind of notation that how my class has stored all of variables i just want to know that how my class is understand those variables.
#So if you want to know of those things 
print(M.__dict__.keys())
#This going to gives you the all variable name. This is applibcable for all the classes.
#Basically your class is trying to understand this variable, So whenever i'm trying to define a variable(__name)so internally class always trying to append __variable.
#So whenever you want to access the private variable you have to give in this way.
print(M._Mar__name)


# In[23]:


#No Static keyword in Python, this keyword,constructor, final, private, protected , public not availble in python oops pgmg

#Self is not a keyword it just a name for the reference of pointer

#dir class
dir(Jasvee)


# ## Inheritance

# If you are trying to inherit the properties from parent to child class called as inheritance.which means whatever i have created over the parent class if i'm able to access every attributes in the child class.So you are not suppsoed to recreate in the child class you can reuse it.
# 
# Basically Inheritance always try to increase reusability of a code.So instead of writting a code again and again what i vl do is try to inherit it and i vl reuse the code. 

# In[51]:


#Here i'm creating the new class Student and i inheriting the class called Amar
class Student(Amar):
    #Here i inherit all the attributes and methods from the Amar to Student class.
    def __init__(self,stud_id,*args,**kwargs):
        #*args - In my Jasvee class i have some arguments, So pull all those arguments(variables) from Amar class to Student class.
        #Whatever variables in Amar class we are trying to pull all those variables to Student class.
        
        #**kwargs - This is not a mandatory one, and it is a dictionary kind of structure and we have a key and value pairs kind of an argument.
        #If you don't have any key value argument we are not supposed to use this.
        #If we have a dictionary variable use it otherwise leave it, Suppose if you mention there then no pblm it won't harm the execution.
        
            super(Student,self).__init__(*args,**kwargs)
            self._student_id=stud_id
            
            #super is a keyword and self refering to the Amar class(parent class)
            #.__init__ -- So we are trying to  revoke the Amar class __int__ method over here.
            # So super(Student,self).__init__(*args,**kwargs) - whatever attributes or methods in the __init__ in Amar class we are trying to reinitialize the same thing to the Student class.
            # like self.name = name,self.age = age ....
#Here it takes 4 arguments -- 1.Student and 3 from the Amar class            
Ja=Student(1,'JasveeAdithri Amarnath',1,2018)
print(Ja)
print(type(Ja))
#Here i'm trying to check is Ja is a instant of Amar class
print(isinstance(Ja,Amar))
print(isinstance(Ja,object))


# ## Overriding methods
# Here it is simply means we are trying to change a body of a particular method with same function name. 

# In[56]:


class Student(Amar):
    def __init__(self,stud_id,*args,**kwargs):
        super(Student,self).__init__(*args,**kwargs)
        self._student_id=stud_id
    def __str__(self):
        #Here i'm calling Amar class str method and append my new string in to it.
        return super(Student,self).__str__() + " and has id : {}".format(self._student_id)
Jasvee=Student(20,'JasveeAdithri','1',2018)
print(Jasvee)


# ## Encapsulation
# Hiding an implementation. you don't know about the implementation part.which means what are all the things had done in backend things are hidden.
# 
# You will not be able to see the implementation but you can able to call all of those methods.

# In[66]:


class Tyres:
    def __init__(self,branch,belted_bias,opt_pressure):
        self.Branch=branch
        self.Belted_bias=belted_bias
        self.Opt_pressure=opt_pressure
    def __str__(self):
        return("Tyres: \n Tyres: {} \n Belted-Bias: {} \n Optimal-Pressure: {}".format(self.Branch,self.Belted_bias,self.Opt_pressure))
class Engine:
    def __init__(self,fuel_type,noise_level):
        self.Fuel_type=fuel_type
        self.Noise_level=noise_level
    def __str__(self):
        return("Engine: \n Fuel Type : {} \n Noise-Level : {} ".format(self.Fuel_type,self.Noise_level))
class Body:
    def __init__(self,size):
        self.size=size
    
    def __str__(self):
        return("Car body: \n Body size: {}".format(self.size))
class Car:
    def __init__(self,tyres,engine,body):
        self.Tyres=tyres
        self.Engine=engine
        self.Body=body
    
    def __str__(self):
        return str(self.Tyres) + "\n" + str(self.Engine) + "\n" + str(self.Body)
T= Tyres('Michillein',True,32.0)
E=Engine("Diesel",'Medium')
B=Body('Medium')
#Here i'm passing the object of Tyre,Engine and Body class to the Car class object, instead of string or int i'm passing directly the objects.
C=Car(T,E,B)
print(C)


# ## Polymorphism and Duck typing
# Consider me i am a father of someone, i'm a son of some one, i'm a husband of some one. In a different situations i behave or act accordingly. A single person but have different emotions or habits or role based on situation. one object but it bahaves different different situations.

# In[67]:


#Here behaviour is going to change but the entity is not going to change. Here + operator basically a polymorphism operator  
def summer(a,b):
    return a+b
print(summer(1,1))
print(summer(["a",'b','c',"d"],["e",'f']))
print(summer("jasvee","Adithri"))


# In[ ]:


#We are just trying to reuse the classes which is already being created and i'm not supposed to recreate those classes again.

