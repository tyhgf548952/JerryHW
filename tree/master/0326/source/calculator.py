
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


def calculator(num1,num2):
    op = input("請輸入加減乘除的符號(+,-,*,/) : ")
    print(calculate(op,num1,num2))