import pandas as pd
from konlpy.tag import Okt
from gensim.models.word2vec import Word2Vec
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pickle
from PIL import Image
import numpy as np

tagger = Okt()

stop_words = '등 것 이 말 명 전 그 고 위 때문 마련 저 라고 수 기자'
stop_words = stop_words.split(' ')

kw = '창업'
corpus = list(pd.read_csv('NaverNews_{0}.csv'.format(kw))['content'].values)
corpus = [[word for word in tagger.nouns(line) if word not in stop_words] for line in corpus]

print(len(corpus))

word_list = sum(corpus, [])
counts = Counter(word_list)
tags = counts.most_common(50)

with open(file='counts.pickle', mode='wb') as f:
    pickle.dump(counts, f)

wc = WordCloud(background_color='White', width=1300, height=1300, scale=2.0, max_font_size=250,
               font_path='/home/invalidid56/MaruBuri-Light.otf', colormap='PuBu')

cloud = wc.generate_from_frequencies(dict(tags))

plt.figure(figsize=(10, 8))
plt.axis('off')
plt.imshow(cloud)
plt.show()

