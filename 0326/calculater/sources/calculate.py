
# coding: utf-8

# In[16]:


def calculate(operator,num1,num2):
    if operator== "+":
        return num1+num2
    elif operator=="-":
        return num1-num2
    elif operator=="*":
        return num1*num2
    elif operator=="/":
        return num1/num2


# In[17]:


def calculater(num1,num2):
    op = input("請輸入加減乘除的符號(+,-,*,/) : ")
    print(calculate(op,num1,num2))


# In[19]:


calculater(2,3)


# In[3]:


calculater(2,3,4)


# In[13]:


calculater(5,6)

