#!/usr/bin/env python
# coding: utf-8

# 
# <a href='https://www.darshan.ac.in/'> <img src='https://www.darshan.ac.in/Content/media/DU_Logo.svg' width="250" height="300"/></a>
# <pre>
# <center><b><h1>Python Programming - 2301CS404</b></center>
# <center><b><h1>Lab - 2</b></center>    
# <pre>

# # if..else..

# ### 01) WAP to check whether the given number is positive or negative.

# In[2]:


x= int(input("enter the number "))
if x<0:
 print('number is negative')   
 
else:
    print('the number is positve')
    
 


# ### 02) WAP to check whether the given number is odd or even.

# In[4]:


x=int(input("enter thenumber"))

if x%2==0 :
    print("the number is even")
    
else :
    print("the number is odd")


# ### 03) WAP to find out largest number from given two numbers using simple if and ternary operator.

# In[15]:


x= int(input('the number is '))

y= int(input("the number 2 "))

# if x < y :
#     print('the y is largest')
# else :
#     print('the x is largest')

print('the y is largest') if  (x < y) else print('the x is largest')
   


# ### 04) WAP to find out largest number from given three numbers.

# In[18]:


x= int(input('the number is '))

y=int(input("the number 2 "))

z= int(input('the number 3 '))

if(x > y) :
    if (x >z):
        print('the x is largest')
        
    else :
        print('the z is largest')
elif(y > x):
    if(y > z): 
        print("the y is largest")
    else :
        print('the z is largest')


# ### 05) WAP to check whether the given year is leap year or not.
# [If a year can be divisible by 4 but not divisible by 100 then it is leap year but if it is divisible by 400 then it is leap year]

# In[21]:


x= int(input('the number is '))

if (x %4==0 and x % 100 !=0) or x%400 ==0 :
    print('leap')
else:
    print("not leap")


# ### 06) WAP in python to display the name of the day according to the number given by the user.

# In[26]:


n=int(input("enter the number"))

match n :
    case 0 :
        print('sunday')
    case 1 :
        print('mon')
    case 2:
        print('tues')
    case 3 :
        print('wed')
    case 4 :
        print('thur')
    case 5 :
        print('fri')
    case 6 :
        print('satur')
    
    
    


# ### 07) WAP to implement simple calculator which performs (add,sub,mul,div) of two no. based on user input.

# In[27]:


x = int(input('enter the number ='))
y= int (input('enter the second number ='))
z= input('enter the task')

match z :
    case '+':
        print(x+y)
    case '-':
        print(x-y)
    case '*': 
        print(x*y)
    case '/':
        print(x/y)
    case _ :
        print('invalid')


# ### 08) WAP to read marks of five subjects. Calculate percentage and print class accordingly. 
# Fail below 35 </br>
# Pass Class between 35 to 45 </br>
# Second Class</br>
# between 45 to 60</br>
# First Class between 60 to 70</br> 
# Distinction if more than 70

# In[29]:


a = int(input('enter the 1 number = '))
b= int (input('enter the second number = '))
c = int(input('enter the 3rd number = '))
d= int (input('enter the 4th number = '))
e = int(input('enter the  5th number = '))

avg= (a+b+c+d+e)/5

if avg >70:
    print('distinction')
elif avg >= 60:
    print('the first')
elif avg >= 45:
    print('the second')
elif avg >=35:
    print('the pass')
else:
    print('fail')


# ### 09) Three sides of a triangle are entered through the keyboard, WAP to check whether the triangle is isosceles, equilateral, scalene or right-angled triangle.

# In[32]:


a= int(input('the s1 side'))
b= int(input('the s2 side'))
c= int(input('the s3 side'))

if a==b and b==c :
    print("equilateral")
elif a==b or a==c :
    print('isosceles')
elif a!=b and b!=c and a!=c :
    if(pow(a,2)+ pow(b,2)==pow(c,2) or pow(a,2)+ pow(c,2)== pow(b,2) or pow(b,2)+ pow(c,2)== pow(a,2)):
        print("right angle")
    else :
        print('scalene')


        


# In[ ]:





# ### 10) WAP to find the second largest number among three user input numbers.

# In[34]:


x= int(input('the number is '))

y=int(input("the number 2 "))

z= int(input('the number 3 '))

if x > y :
    if x > z:
        print('the z is largest')
        
    else :
        print('the x is largest')
elif y > x:
    if y > z: 
        print("the z is largest")
    else :
        print('the y is largest')


# ### 11) WAP to calculate electricity bill based on following criteria. Which takes the unit from the user.
# a. First 1 to 50 units – Rs. 2.60/unit</br>
# b. Next 50 to 100 units – Rs. 3.25/unit</br>
# c. Next 100 to 200 units – Rs. 5.26/unit</br>
# d. above 200 units – Rs. 8.45/unit

# In[35]:


unit=int(input('enter the total unit  = '))

bill=0
if unit >200:
    print(f'the bill amount is  = {unit*8.45}', )
elif unit >100:
    print(f'the bill amount is  = {unit*5.36}', )
elif unit > 50:
    print(f'the bill amount is  = {unit*3.25}', )
elif unit >= 1:
    print(f'the bill amount is  = {unit*2.60}', )



# In[ ]:


256

