import pandas as pd
import nltk
import numpy as np
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import pairwise_distances
from hangul.tokenizer import WordSegmenter
from keras.layers import LSTM
from keras.saving import register_keras_serializable
register_keras_serializable()(LSTM)
from konlpy.tag import Okt

df_hangul = pd.read_fwf("korean-story.txt", header='infer', encoding="utf-8")
print(df_hangul.head())

print(df_hangul.shape)
kor_t = Okt()
korean_docs = ["새로운 보금자리",
               "내가 이사를 오고 나서 여동생이 우리 동생은 서울에 있는 대학에 사는 동네가 우리 꽤 멀어서 서로 만나기가 쉽지 않았다",
               "내가 새로 살게된 집은 거실 하나와 방 두 개가 있었고, 앞에는 공영 있었다",
               "주차장에 설치된 CCTV가 24시간 작동하고 있기 때문에 이 집은 더 안전하게 느껴졌다",
               "새 집에는 곰팡이나 벌레도 없었다. 동네가 조용한 것과 주변에 아름다운 피어있는 것도 마음에 들었다",
               "집을 둘러본 동생은 우리의 어린 시절 사진을 보여주겠다며 휴대폰 사진첩을 거기에는 어렸을 때 엄마가 찍어주신 사진들이 해맑게 웃고 있는 어린 아이들이 무척"]

k_tokens = kor_t.morphs("내가 이사를 오고 나서 여동생이 우리 동생은 서울에 있는 대학에 사는 동네가 우리 꽤 멀어서 서로 만나기가 쉽지 않았다")
print(f"Tokens:{k_tokens}")

