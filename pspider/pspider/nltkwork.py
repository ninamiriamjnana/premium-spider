from peeweemodels import *

#!/usr/bin/env python
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import nltk

from nltk import word_tokenize

from nltk import FreqDist

from nltk.collocations import *

# set of stopwords for german
stopset = set(nltk.corpus.stopwords.words('german'))

import csv

def make_nltk_text():

    # query holt text und ordnet nach datum
    textquery=(Post.select(Post.text, Date_Tab.year, Date_Tab.month, Date_Tab.day).join(Date_Tab).naive().order_by(Date_Tab.year, Date_Tab.month, Date_Tab.day))
    s=""    
    for x in textquery:
        t=x.text.encode('utf8')
        s+=str(t)

    tokens=word_tokenize(s)
    text=nltk.Text(tokens)
    words=[w.lower() for w in tokens]

    #ich nehm nur w ab laenge 3
    long_words = [w for w in words if len(w) > 3 and w not in stopset]

    fdist=FreqDist(long_words)
    x=fdist.most_common(100) # sind uninteressant

    # wie hol ich nur ngrams with freuqency mehr als 5
    bigram_measures = nltk.collocations.BigramAssocMeasures()
    trigram_measures = nltk.collocations.TrigramAssocMeasures()
    finderb = BigramCollocationFinder.from_words(long_words)
    finderb.apply_freq_filter(3)
    b=finderb.nbest(bigram_measures.pmi, 100)

    findert = TrigramCollocationFinder.from_words(long_words)
    findert.apply_freq_filter(3)
    t=findert.nbest(trigram_measures.pmi, 100)
   

    #create trigrams and bigrams

    all_trig=nltk.trigrams(long_words)
    all_big=nltk.bigrams(long_words)

    return text
"""
    with open('100mostcommon.csv', 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(x)

    with open('100trigrams.csv', 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(t)

    with open('100bigrams.csv', 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(b)

    with open('allbigrams.csv', 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(all_big)

    with open('alltrigrams.csv', 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(all_trig)
"""

    


