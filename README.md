# Amazon-Review-Classifier
Machine Learning / Data mining - Reads and Labels whether an amazon review is positive or negative. Implements KNN (K nearest neighbors)
to Label review. A molecule can be represented by several thousands of binary features which represent their topological shapes and other characteristics important for binding.

## Dataset
The dataset has an imbalanced distribution 
train - 17,000 amazon reviews; Labels: +1 for positive, -1 for negative. <br />
test - 3,000 amazon reviews no labels.

## Approach
2d array to store each review and word. Rows = reviews, columns = words. Use nltk to extract stop words/punctuation and
stem all words (playing = play | running = run). Use textblob to get polarity of each sentence. Create list of features. Plot, 
if majority near it is positive review is positive otherwise negative.

## Major libraries
textblob <br />
nump y<br />
nltk <br />
sklearn <br />
matplotlib <br />
pandas <br />
