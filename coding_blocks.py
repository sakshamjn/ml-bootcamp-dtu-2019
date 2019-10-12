
# coding: utf-8

# In[1]:


print("hello World!")


# In[2]:


a = input()


# In[5]:


print(a)


# In[4]:


print a


# In[6]:


a = 10
b = 20
print(a+b)


# In[7]:


print(type(a))


# In[9]:


# Execute a shell = shift+enter
# add a cell above   =   Exc + a
# add a cell below   =  Exc+ b


# In[16]:


b = "hello i am Saksham"
b.lower()
b = b.split()


# In[17]:


print(len(b))


# In[18]:


for word in b:
    print(word)


# In[21]:


a = "  hello Wordl"
print(len(a))


# In[22]:


a = a.strip()
print(a)
print(len(a))


# In[31]:


#slicing
print(a[3:5])
print(a[:-3])
a[-2]
print(a[-3: :2]) # for getting alternate nos.


# In[ ]:


## DATA Structure

    #List
L = [1, 2, 3, 4, 5, 6]
print(type(L))


# In[41]:


L.append(10)  #  element added
L.pop(0) # Location removed
#  HELP   L.remove?  
L.remove(6)


# In[42]:


L


# In[43]:


L.clear


# In[44]:


## Dictonaries  in python
price_table = {
    "sweets":40,
    "namkeen":20
}
price_table["halwa"] = 30


# In[45]:


print(price_table)


# In[47]:


price_table["halwa"]


# In[48]:


print(price_table.get("namkeen"))


# In[49]:


price_table.keys()


# In[51]:


price_table.values()


# In[52]:


a = ["India","Japan", "USA"]
b = ["Delhi", "tokyo","washington"]
d = dict(zip(a,b))
print(d)


# In[53]:


d["India"]


# In[ ]:


for i in range(0,10):
    print(i)


# In[ ]:


for i in range(0,10,3):
    print(i **2)
    break


# In[ ]:



for i in range(5):
    for j in range(i):
        print("*",end ="")
    print("\n")
        


# In[ ]:


for i in range(1,5):
    print("*"*i)


# In[ ]:


with open("sam")


# In[ ]:


with open("untitled.txt") 


# In[ ]:


def load_words(filename):
    f = open(filename,"r")
    return f.read.split() 


# In[ ]:


print(load_words("untitled.txt"))

