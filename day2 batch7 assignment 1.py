#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# list



lst = ["anchal","mohan",0.1,7,28]


# In[2]:


lst


# In[3]:


lst[1]  


# In[4]:


lst.append("letsupgrade")


# In[5]:


lst


# In[6]:


lst.clear()


# In[7]:


lst


# In[8]:


lst = ["anchal","mohan","letsupgrade","python",22.47845]


# In[9]:


lst.copy()


# In[10]:


lst=[123, 'xyz', 'zara', 'abc', 123]


# In[11]:


lst.count("zara")


# In[12]:


lst.extend("nike")


# In[13]:


lst


# In[16]:


lst.index(123)


# In[15]:


lst


# In[20]:


lst.insert(4,10)


# In[21]:


lst


# In[22]:


lst.pop()


# In[23]:


lst


# In[24]:


lst.remove(10)


# In[25]:


lst


# In[26]:


lst.reverse()


# In[27]:


lst


# In[30]:


lst = [7,5,0,4,8,3,2,1,6]


# In[31]:


lst.sort()


# In[32]:


lst


# # Dictionary

# In[33]:


dit = {1:"I",2:"am",3:"learning",4:"python"}


# In[35]:


dit


# In[36]:


dit.get(1)   


# In[37]:


dit.pop(3)   


# In[40]:


dit.copy()


# In[41]:


dit1={"Name":"Anchal"}


# In[49]:


dit1


# In[53]:


dit


# In[54]:


dit.update(dit1)


# In[55]:


dit


# In[56]:


dit.items()


# # sets

# In[57]:


st = {"anchal","mohan",1,1,1,3,3,3,5,5,0,0,3,7,7,7,7,7}


# In[58]:


st


# In[59]:


st.add(8)


# In[60]:


st


# In[63]:


st1={"anchal",7}


# In[64]:


st1.issubset(st)


# In[65]:


st1.clear()


# In[66]:


st1


# In[67]:


stA = {10, 20, 30, 40, 80}


# In[68]:


stB = {100, 30, 80, 40, 60}


# In[69]:


stA.difference(stB)


# In[70]:


stA.discard(10)


# In[71]:


stA


# # tuple

# In[73]:


tup = ("python","programming","letsupgrade")


# In[74]:


tup


# In[75]:


tup.count("programming")


# In[76]:


tup.index("programming")


# # String

# In[77]:


name = "Anchal mohan"
name1 = "is "


# In[78]:


name


# In[81]:


str.capitalize("mohan")


# In[91]:


str = "this is string example....wow!!!"


# In[92]:


sub = "i"


# In[93]:


str.count(sub, 4, 40)


# In[97]:


str.center(40, 'a')


# In[98]:


str2 = "exam"


# In[100]:


str1 = "this is string example....wow!!!"


# In[101]:


str1.find(str2)


# In[102]:


str1.find(str2, 10)


# In[103]:


str1.index(str2)


# In[ ]:




