#!/usr/bin/env python
# coding: utf-8

# In[14]:


'''Q1. You are writing code for a company. The requirement of the company is that you create a
python  function that will check whether the password entered by the user is correct or not. 
The function should  take the password as input and return the string “Valid Password” if the
entered password follows the  below-given password guidelines else it should return “Invalid Password”. 
Note: 1. The Password should contain at least two uppercase letters and at least two lowercase letters.
2. The Password should contain at least a number and three special characters. 
3. The length of the password should be 10 characters long. 
'''
password=input('Enter password')
lowercase=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
uppercase=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['1','2','3','4','5','6','7','8','9']
special_character=['!','@','#','$','%','^','&','*']
l,u,n,s,length=0,0,0,0,0
for i in password:
    if i in lowercase:
        l+=1
    if i in uppercase:
        u+=1
    if i in numbers:
        n+=1
    if i in special_character:
        s+=1
    if len(password)==10:
        length+=1
if (l>=2 and u>=2 and n>=1 and s>=3 and length>=1 ):
    print('Valid password')
else:
    print('Invalid password')


# In[32]:


'''Q2. Solve the below-given questions using at least one of the following:  
1. Lambda function 
2. Filter function 
3. Map function 
4. List Comprehension 
 Check if the string starts with a particular letter 
 Check if the string is numeric 
 Sort a list of tuples having fruit names and their quantity. [("mango",99),("orange",80), ("grapes", 1000)  
 Find the squares of numbers from 1 to 10 
 Find the cube root of numbers from 1 to 10 
 Check if a given number is even 
 Filter odd numbers from the given list. 
 [1,2,3,4,5,6,7,8,9,10 
 Sort a list of integers into positive and negative integers lists. 
 [1,2,3,4,5,6,-1,-2,-3,-4,-5,0] 
'''
#check if the string starts with a particular letter lets say 'm' using lambda function
s=input('Enter any string')
letter=lambda s:s.startswith(('m','M'))
letter(s)


# In[21]:


#Check if the string is numeric using lambda function
s=input('Enter any string')
number=lambda s:s.isnumeric()
number(s)


# In[34]:


#Sort a list of tuples having fruit names and their quantity. [("mango",99),("orange",80), ("grapes", 1000)] using lambda function
l=[("mango",99),("orange",80), ("grapes", 1000)]
sorting=sorted(l,key=lambda x:x[1])
sorting


# In[35]:


# Find the squares of numbers from 1 to 10 using list comprehension
[i**2 for i in range(1,11)]


# In[36]:


#Find the cube root of numbers from 1 to 10 using list comprehension
[i**3 for i in range(1,11)]


# In[39]:


#Check if a given number is even using lambda function
x=int(input('Enter number'))
even=lambda x:x%2==0
even(x)


# In[43]:


# Filter odd numbers from the given list. [1,2,3,4,5,6,7,8,9,10] using filter and lambda function
l=[1,2,3,4,5,6,7,8,9,10]
list(filter(lambda x:x%2 !=0,l))


# In[51]:


# Sort a list of integers into positive and negative integers lists. [1,2,3,4,5,6,-1,-2,-3,-4,-5,0] using list comprehension
l=[1,2,3,4,5,6,-1,-2,-3,-4,-5,0] 
positive_list=[i for i in l if i>=0]
negative_list=[i for i in l if i<0]
print(positive_list)
print(negative_list)


# In[ ]:




