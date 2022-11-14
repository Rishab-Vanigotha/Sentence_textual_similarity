# Sentence_textual_similarity
Part _A:
	In part_A, firstly we import all the necessary libraries like Pandas for data manipulation and sentence_transformer and Sklearn.metrics for evaluation using cosine similarity.
	Then import the Precily text similarity dataset and load pretrained model to perform sentence embedding. I have used “all-MiniLM-L6-v2” hugging face model to embed the sentences of text1 and text2 column of the dataset.
	Sentence embeddings in NLP is used to map the sentences to vectors of real numbers 
	Then creating a new column to store the sentence similarity values computed using cosine similarity from pairwise library of sklearn module
	Rounding off the cosine similarity values from [-1, 1] to [0, 1], where 0 means sentences are highly dissimilar and 1 means sentences are highly similar.
Part_B:
	Deploying the Part_A algorithm in Heroku(by salesforce) cloud server.
	I have used streamlit module to build the app which takes two sentences as input and respond the similarity score between the two sentences
	Streamlit app is then hosted on heroku using github respository.
	The final Server API Endpoint is as follows:
	https://sentencesimilaritynlp.herokuapp.com
 
