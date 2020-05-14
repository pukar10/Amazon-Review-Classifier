# Amazon-Review-Classifier
Machine Learning / Data mining - Reads and Labels whether an amazon review is positive or negative. Implements KNN (K nearest neighbors)
to Label review.

Dataset
train - 17,000 amazon reviews; Labels: +1 for positive, -1 for negative. 
test - 3,000 amazon reviews no labels.

Approach
2d array to store each review and word. Rows = reviews, columns = words. Use nltk to extract stop words/punctuation and
stem all words (playing = play | running = run). Use textblob to get polarity of each sentence. Create list of features. Plot, 
if majority near it is positive review is positive otherwise negative.

Major libraries
textblob
numpy
nltk
sklearn
matplotlib
pandas
