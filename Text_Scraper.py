#Code written by Shimon Johnson
#!/usr/bin/env python
# coding: utf-8

# In[53]:


import urllib
from bs4 import BeautifulSoup



url = "file:///Users/shimonjohnson/Downloads/docs-2/api/java/util/ServiceConfigurationError.html"
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html)

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = list(line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)
ans = []
for line in lines:
    if line != "":
        ans.append(line)


# In[54]:


with open('your_file.txt', 'w') as f:
    for item in ans:
        f.write("%s\n" % item)


# In[ ]:
