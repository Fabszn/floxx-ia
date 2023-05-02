#!/usr/bin/env python
# coding: utf-8

# In[6]:


# In[7]:


import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
from IPython.display import Image, display


# In[8]:
model_cfg = 'path/to/yolov4.cfg'
model_weights = 'path/to/yolov4.weights'
net = cv2.dnn.readNetFromDarknet(model_cfg, model_weights)

IMAGE_SOURCE = "../../pictures/test3.jpeg"
IMAGE_OUT = "test3_out.jpeg"


# In[9]:


display(Image(IMAGE_SOURCE))


# In[58]:


img = cv2.imread(IMAGE_SOURCE)
print(img)
image_normalisee = cv2.normalize(img, None, 0, 1, cv2.NORM_MINMAX)
res_img = cv2.resize(img, (416,416))
bbox, label, conf = cv.detect_common_objects(res_img, confidence=0.1, model='yolov5')


# for l, c in zip(label, conf):
#     if l == "person":
#         print(f"label {l} confidence {c}")

# In[60]:


filtered = filter(lambda l: l == "person", label)
len(list(filtered))


# In[48]:
#draw box on image
imaFrwed = draw_bbox(res_img, bbox, label, conf)
cv2.imwrite(IMAGE_OUT,imaFrwed)


# In[49]:


display(Image(IMAGE_OUT))


# In[ ]:




