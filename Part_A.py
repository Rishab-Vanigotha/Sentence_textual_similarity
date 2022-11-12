import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
df = pd.read_csv('../input/precily/Precily_Text_Similarity.csv')
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
embed1 = model.encode(list(df['text1']))
embed2 = model.encode(list(df['text2']))
for i in range(len(df)):
    df.loc[i, 'cosine_similarity'] = cosine_similarity([embed1[i]], [embed2[i]])[0][0]
df['cosine_similar'] = df['cosine_similarity'].apply(lambda x: 0 if(x<=0) else x)
print(df)