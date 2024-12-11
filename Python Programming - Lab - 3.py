#!/usr/bin/env python
# coding: utf-8

# 
# <a href='https://www.darshan.ac.in/'> <img src='https://www.darshan.ac.in/Content/media/DU_Logo.svg' width="250" height="300"/></a>
# <pre>
# <center><b><h1>Python Programming - 2301CS404</b></center>
# <center><b><h1>Lab - 3</b></center>    
# <pre>

# # for and while loop

# ### 01) WAP to print 1 to 10.

# In[83]:


for i in range(1,11):
    print(i,end=' ')


# ### 02) WAP to print 1 to n.

# In[84]:


x = int(input('enter the n = '))

for i in range(1,x):
    print(i,end=' ')


# ### 03) WAP to print odd numbers between 1 to n.

# In[85]:


x= int(input('enter the the number opf n = '))

for i  in range(1,x+1):
    if i%2!=0 :
        print(i,end=" ")


# ### 04) WAP to print numbers between two given numbers which is divisible by 2 but not divisible by 3.

# In[ ]:


a = int(input('enter the number  1  = '))
b = int(input('enter the number  2  = '))


for i in range(a,b):
    if(i%2==0 and i%3!=0):
        print(i,end=' ')


# ### 05) WAP to print sum of 1 to n numbers.

# In[26]:


c = int(input("enter the number of "))
sum=0;
for i in range(1,c+1):
        sum+=i
print("the sum of 1 to ",n, "is = ",sum)


# ### 06) WAP to print sum of series 1 + 4 + 9 + 16 + 25 + 36 + ...n.

# In[27]:


d = int(input("enter the number"))

sum=0;
for i in range(d+1):
    sum+=pow(i,2)
print("the sum of the series is = ",sum)
    


# ### 07) WAP to print sum of series 1 – 2 + 3 – 4 + 5 – 6 + 7 ... n.

# In[28]:


e= int(input("enter the number of n "))

sum=0

for i in range(1, e+1) :
    if(i%2==0):
        sum-=i
    else:
        sum+=i
print("print the numbe roif series is ",sum)


# ### 08) WAP to print multiplication table of given number.

# In[37]:


a = int(input("enter the number of n"))

for i in range(1,a+1):
      print(a, '* ', i, " = ", a*i )


# ### 09) WAP to find factorial of the given number.

# In[38]:


x = int(input("enter the number to find the factorial "))

fac=1;
for i in range(1,x+1):
    fac*=i
print("the factorial is = ",fac)


# ### 10) WAP to find factors of the given number.

# In[ ]:


y = int(input("enter the number "))

for i in range(1,y+1):
    if y % i==0 :
        print(i,end=" ")


# ### 11) WAP to find whether the given number is prime or not.

# In[52]:


x = int(input("enter the number to check prime number or not = "))

for i in range(2,x):
    if x % i==0 :
        print('not prime number')
        break;
else :
    print("prime")
  


# ### 12) WAP to print sum of digits of given number.

# In[57]:


x= int(input("enter the number "))
sum=0
while(x !=0):
    r= x%10;
    sum +=r
    x=x/10
print("print the sum of digit is = ",int(sum))


# ### 13) WAP to check whether the given number is palindrome or not

# In[73]:


x= int(input("enter the number "))
z=x
num=0
while(x !=0):
    r= x % 10
    num = num*10+ r
    x=int(x/10)
    
if(num ==z):
    print("the number is palindrome")
else :
    print("the number is not palindrome")


# ### 14) WAP to print GCD of given two numbers.

# In[ ]:


a = int(input("enter the number of 1 = "))
b = int(input("enter the number of 2 = "))
c=[]
gcd=1
for i in range(1, min (a,b)):
    if a % i==0 and b % i ==0:
        gcd=i
print("the gcd od the given number is = ",gcd)


    


# In[ ]:




