#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pathlib import Path
import pandas as pd
import glob


# In[2]:


score_file_path = "Filtered_files/*.csv"
pos_tag_file_path = "POS_output/*.txt"


# In[3]:


score_files = glob.glob(score_file_path)
score_files.sort()
pos_tag_files = glob.glob(pos_tag_file_path)
pos_tag_files.sort()


# In[4]:


Path("./Required_results").mkdir(parents=True, exist_ok=True)


# In[5]:


for i in range(0,len(pos_tag_files)):
    df_temp = pd.read_csv(score_files[i])
    d = []
    track = {}
    with open(pos_tag_files[i], "r") as f:
        for line in f.readlines():
            temp = line.split(",")
            word = temp[0].replace("[","").replace("(","").replace("'","")
            if len(temp) > 1:
                tag = temp[1].replace("[","").replace("(","").replace("'","").replace(")","").replace("-","").replace("$","")
                if tag[1:] == "IN" or tag[1:] == "DT" or tag[1:] == "WDT" or tag[1:] == "PRP" or tag[1:] == "PRP$" or tag[1:] == "WP" or tag[1:] == "WP$" or tag[1:] == "CC" or tag[1:] == "RP" or tag[1:] == "TO" or tag[1:] == "PDT" or tag[1:] == "WRB" or tag[1:] == "MD" or tag[1:] == "CD":
                    df_filtered = df_temp.loc[df_temp['term'].str.lower() == word[1:].lower(), :]
                    
                    
                    if len(df_filtered['score'].values) > 0:
                        if word[1:].lower() not in track:
                            item = {}
                            item['term'] = word[1:]
                            item['score'] = df_filtered['score'].values[0]
                            item['Df'] = df_filtered['Df'].values[0]
                            item['idf'] = df_filtered['idf'].values[0]
                            d.append(item)
                            ans_df = pd.DataFrame(d)
                            ans_df.to_csv("Required_results/file_{}.csv".format(i+1))
                            track[word[1:].lower()] = 1
                    
                    
        


# In[ ]:




