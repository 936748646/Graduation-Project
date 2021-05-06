import sys
import csv
import math
from gensim.corpora.dictionary import Dictionary
from gensim.models.ldamodel import LdaModel

args = sys.argv

dir = args[2]
vec_dir = args[3]

print("Reading preprocessed test cases ...", file=sys.stderr)
texts = []
with open(args[1]) as table_file:
    reader = csv.reader(table_file)
    for row in reader:
        with open(dir + "/" + row[0] + ".txt") as txt_file:
            token_list = []
            for token in txt_file:
                token = token.replace('\n','')
                token = token.replace('\r','')
                token_list.append(token)
            texts.append(token_list)

dictionary = Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]

n_topics = math.floor(len(texts)/2.5)
if ( n_topics - len(texts)/2.5) >= 0.5:
    n_topics = n_topics + 1

print("Making topic model and Computing vectors of test cases ...", file=sys.stderr)
for cnt in range(30):
    print("[" + str(cnt) + "]", file=sys.stderr)
    lda = LdaModel(corpus, num_topics=n_topics, minimum_probability=0, random_state=cnt)
    with open(vec_dir + "/" + str(cnt) + ".csv", mode='w') as vec_file:
        for c in corpus:
            is_first = True
            for pair in lda[c]:
                if is_first:
                    is_first = False
                else:
                    vec_file.write(",")
                vec_file.write(str(pair[1]))
            vec_file.write("\n")
