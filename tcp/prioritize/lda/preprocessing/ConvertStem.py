import sys
from nltk.stem.porter import PorterStemmer as PS
from nltk.corpus import stopwords


ps = PS()
stop_words = stopwords.words('english')
stop_words.append('cannot')

for token in sys.stdin:
    token = token.rstrip('\n')
    token = token.rstrip('\r')

    token = token.lower()

    token = token.replace('\'m','')
    token = token.replace('\'ll','')
    token = token.replace('\'d','')
    token = token.replace('\'ve','')
    token = token.replace('\'re','')
    token = token.replace('\'s','')

    if token.endswith('n\'t') or (token in stop_words):
        continue

    stemmed_token = ps.stem(token)
    if token == stemmed_token:
        print(token)
    else:
        print(stemmed_token)
        