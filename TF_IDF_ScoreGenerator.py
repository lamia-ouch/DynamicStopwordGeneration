#Code written by Shimon Johnson,Matthew Lavin
#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pathlib import Path
import numpy as np
import pandas as pd

all_txt_files =[]
for file in Path("Input_files").rglob("*.txt"):
     all_txt_files.append(file.parent / file.name)
# counts the length of the list
n_files = len(all_txt_files)
print(n_files)


# In[2]:


all_txt_files.sort()
all_txt_files[0]


# In[3]:


all_docs = []
for txt_file in all_txt_files:
    with open(txt_file) as f:
        txt_file_as_string = f.read()
    all_docs.append(txt_file_as_string)


# In[4]:


#import the TfidfVectorizer from Scikit-Learn.
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(max_df=1.0, min_df=1, stop_words=None, use_idf=True)
transformed_documents = vectorizer.fit_transform(all_docs)


# In[5]:


transformed_documents_as_array = transformed_documents.toarray()
# use this line of code to verify that the numpy array represents the same number of documents that we have in the file list
len(transformed_documents_as_array)


# In[6]:


idf_value = vectorizer.idf_


# In[7]:


N = transformed_documents_as_array.shape[0]
Df = ((N+1)/ (np.exp(idf_value)/ np.exp(1)))


# In[8]:


# make the output folders if it doesn't already exist
Path("./Scored_files").mkdir(parents=True, exist_ok=True)
Path("./Filtered_files").mkdir(parents=True, exist_ok=True)


# In[9]:


# construct a list of output file paths using the previous list of text files the relative path for tf_idf_output
output_filenames = [str(txt_file).replace(".txt", ".csv").replace("Input_files/", "Scored_files/") for txt_file in all_txt_files]

# loop each item in transformed_documents_as_array, using enumerate to keep track of the current position
for counter, doc in enumerate(transformed_documents_as_array):

    # constructing dataframe
    tf_idf_tuples = list(zip(vectorizer.get_feature_names(), doc, np.round(Df-1)))
    one_doc_as_df = pd.DataFrame.from_records(tf_idf_tuples,columns=['term', 'score', 'Df']).sort_values(by='score', ascending=False).reset_index(drop=True)
    one_doc_as_df = one_doc_as_df[one_doc_as_df['score']>0]
    one_doc_as_df['std'] = one_doc_as_df['score'].std()
    one_doc_as_df['mean'] = one_doc_as_df['score'].mean()
    one_doc_as_df['idf'] = idf_value[one_doc_as_df.index]


    print(counter, one_doc_as_df.shape)
    one_doc_as_df.to_csv(output_filenames[counter], index=False)
    #one_doc_as_df['sum_mean_std'] = one_doc_as_df['mean'] + one_doc_as_df['std']
    one_doc_as_df['sec_std'] = (one_doc_as_df['mean'] + (2*(one_doc_as_df['std'])))
    one_doc_as_df[one_doc_as_df['score'] < one_doc_as_df['sec_std'] ].to_csv('Filtered_files/{}.csv'.format(counter+1))


# In[ ]:
