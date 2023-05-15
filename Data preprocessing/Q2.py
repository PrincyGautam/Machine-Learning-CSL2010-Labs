#!/usr/bin/env python
# coding: utf-8

# In[4]:


from PIL import Image 
import PIL 
img = Image.open(r"C:\Users\HP\OneDrive\Pictures\Camera Roll\Pic.jpg") 
img = img.save("PIC.jpg")

