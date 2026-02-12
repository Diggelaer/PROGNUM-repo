#!/usr/bin/env python
# coding: utf-8

# Answers for Week 1
# 
# * Name: Sappho Visser
# * Username: djvisser
# * Student s-number: s6406734
# * Group (AS1, etc.): AS5

# In[6]:


x=22/7


# $$y=\frac{sin(x)}{x}$$

# In[7]:


pi = 22/7


# ![moon.png](attachment:7326a6dd-486c-44df-b15e-2ba303a7303a.png)

# In[11]:


fact = 6
for i in range(5):
    fact *= i+1
print(fact)


# In[13]:


from scipy.constants import c, h
f = 2.42*10**28
E = h*c*f
print(E)


# In[17]:


from scipy.constants import G
m_1 = 5.9722*10**24
m_2 = 7.342*10**22
r = 385000.6*10**3
F = G*((m_1*m_2)/(r**2))
print(F)


# In[18]:


x1 = 10
x2 = 22/7
print(x1, end="")
print(x2, end="")

