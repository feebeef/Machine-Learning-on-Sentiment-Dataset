#!/usr/bin/env python
# coding: utf-8

# In[17]:


# Import Packages
import pandas as pd
import spacy

# Used for plotting
import matplotlib.pyplot as plt


# In[ ]:


# Declare functions
def tokenize_spacy(text, nlp):
    doc = nlp(text)
    return [token.text for token in doc]

def lemmatize_spacy(text, nlp):
    doc = nlp(text)
    return [token.lemma_ for token in doc]


# In[2]:


# Load the Data
df = pd.read_csv('gamespot_reviews.csv').iloc[:50]
df.head()


# In[4]:


# Load Spacy Multi-task Convolutional Neural Network Model
# This is a neural network model (aka "AI") that was trained to perform the basic NLP pipeline
nlp = spacy.load("en_core_web_sm")

# Execute the pipeline
df['tokenized'] = df['text'].apply(lambda x: tokenize_spacy(x, nlp))
df['lemmatized'] = df['text'].apply(lambda x: lemmatize_spacy(x, nlp))


# In[5]:


print(df.text[0][:125])


# In[6]:


print(df.tokenized[0][:25])


# In[7]:


# Bonus knowledge:
# Notice how "Obduction" is still capitalized, whereas "towards" is not.
# The NN executed the casefolding alongside with lemmatization whilst also considering if the word is a Proper Noun.
print(df.lemmatized[0][:25])


# In[22]:


# Visualiation
fig, ax = plt.subplots(figsize=(6,3), dpi=120)
pd.DataFrame(df.lemmatized.apply(lambda x: len(set(x)))).join(df.tokenized.apply(lambda x: len(set(x)))).iloc[:5].sort_values('tokenized').plot(kind='barh', ax=ax)
ax.set_ylabel('Document Number')
ax.set_xlabel('Token Count')
ax.set_title('First 5 Documents')


# In[ ]:




