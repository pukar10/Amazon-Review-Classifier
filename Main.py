import random
from operator import itemgetter

import numpy
import nltk
import sklearn
# import Re
import scipy
import matplotlib
import os
import string
import pandas
import textblob
import scipy
from scipy.spatial import distance
from collections import Counter, OrderedDict

# Re
# nltk.stopwords() kills useless words
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from textblob import TextBlob


def main():
    k = 11
    reviewType = []
    trainSet = []
    testSet = []
    dictionary = {'polarity'}  # label for each feature

    n = 0
    with open('train_file_test.dat', "r") as f:
        for line in f:
            # CATEGORIZE each review AND tokenize each word AND lower case AND remove punctuation
            if line[0] == '+':
                reviewType.append(True)
            else:
                reviewType.append(False)

            # tokenize sentence | lower case | remove punctuation
            words = line.split()
            words = [word.lower() for word in words]
            table = str.maketrans('', '', string.punctuation)
            words = [w.translate(table) for w in words]

            # stemming each word. Creating new working list pWords.
            ps = nltk.PorterStemmer()
            pWords = []
            for word in words:
                pWords.append(ps.stem(word))

            # download list of stopwords
            # nltk.download('stopwords')
            stop_words = stopwords.words('english')
            pWords = [word for word in pWords if word not in stop_words]

            # FEATURES ----
            trainVector = []
            blob = TextBlob(' '.join(pWords))

            # Polarity of sentence
            polarity = blob.polarity
            trainVector.append(polarity)
            trainSet.append(trainVector)



    # test file into vectors for testing
    with open('test_test.dat', 'r') as x:
        for line in x:
            words = line.split()
            words = [word.lower() for word in words]
            table = str.maketrans('', '', string.punctuation)
            words = [w.translate(table) for w in words]

            # stemming each word. Creating new working list pWords.
            ps = nltk.PorterStemmer()
            pWords = []
            for word in words:
                pWords.append(ps.stem(word))

            # download list of stopwords
            # nltk.download('stopwords')
            stop_words = stopwords.words('english')
            pWords = [word for word in pWords if word not in stop_words]

            # FEATURES
            # 1 POLARITY OF SENTENCE
            testVector = []
            blob = TextBlob(' '.join(pWords))
            # blob = blob.correct()
            # send vector to dictionary
            testVector.append(blob.polarity)
            testSet.append(testVector)

    # KNN get all distances | sort | get K neighbors |
    # save all distances and index in d
    # d holds index of point in train and distance from predicted point
    d = []
    n = 0
    for x in testSet:
        for y in trainSet:
            # TESTING
            if x is None or y is None:
                print(n)
                print(x, y)
            # --------
            d.append([n, distance.euclidean(x, y)])
            n += 1
    d = sorted(d, key=itemgetter(1))

    # get k neighbors
    neighbors = d[0:k]

    # will print the k nearest points (trainSet) to the predicted point (testSet)
    # check if neighbors are positive or negative increment count
    pCount = 0
    nCount = 0
    for lists in range(len(neighbors)):
        tempList = neighbors[lists]
        index = tempList[0]
        trainSet[index]
        print(reviewType[index]) # print to see points near test point are pos or neg
        if reviewType[index] is True:
            pCount += 1
        else:
            nCount += 1

    print('POS: ' + str(pCount) + ' NEG:' + str(nCount))
    # count positive and negative votes. Determine pos or neg for test point.
    if pCount > nCount:
        results = open("Results,txt", "w")
        results.write('+1\n')
    else:
        results = open("Results,txt", "w")
        results.write('-1\n')


if __name__ == "__main__":
    main()
