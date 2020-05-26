#Code written by Shimon Johnson
#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.feature_extraction import stop_words
import pandas as pd


# In[2]:


d= []


# In[3]:


d.append(stop_words.ENGLISH_STOP_WORDS)


# In[4]:


ans_df = pd.DataFrame(d)


# In[5]:


ans_df.to_csv("SCIKIT_STP_LIST.csv")


# In[ ]:
