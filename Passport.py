#!/usr/bin/env python
# coding: utf-8

# In[5]:


import cv2

img = cv2.imread("passport.png")
    


# In[6]:


img


# In[1]:


import matplotlib.pyplot as plt


# In[13]:


import cv2

img = cv2.imread("passport.png")
plt.imshow(img)


# In[4]:


img.shape


# In[5]:


from pytesseract import pytesseract


# In[6]:


import os


# In[7]:


import pytesseract


# In[8]:


from PIL import Image


# In[12]:


from PIL import Image
from pytesseract import pytesseract

#Define path to tessaract.exe
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#Define path to image
path_to_image = 'passport.png'

#Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract

#Open image with PIL
img = Image.open(path_to_image)

#Extract text from image
text = pytesseract.image_to_string(img)

print(text)

