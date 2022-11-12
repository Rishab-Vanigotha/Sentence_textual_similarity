# Importing necessary Libraries
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
# Loading the dataset
df = pd.read_csv('C:\Users\DELL\Desktop\Precily_Task\Precily_Task\Precily_Text_Similarity.csv')

# Loading the pre-trained model from sentence transformers
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Creating embeddings for the sentences in dataset
embed1 = model.encode(list(df['text1']))
embed2 = model.encode(list(df['text2']))

# Creating a column for the cosine similarity
for i in range(len(df)):
    df.loc[i, 'cosine_similarity'] = cosine_similarity([embed1[i]], [embed2[i]])[0][0]

# creating a new column for the rounded cosine similarity values from [-1, 1] to [0, 1]
df['cosine_similar'] = df['cosine_similarity'].apply(lambda x: 0 if(x<=0) else round(x,2))

print(df)