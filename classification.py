#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
import pickle

from sklearn.metrics import classification_report,confusion_matrix,accuracy_score

from train_testsplit import train_reviews,test_reviews,train_sentiments,test_sentiments
type (test_reviews)

tf=TfidfVectorizer(min_df=5,max_df=0.8,ngram_range=(1,3),use_idf=True,analyzer='word')
tff =tf.fit(train_reviews)
tftrain_reviews=tff.transform(train_reviews)
tftest_reviews=tff.transform(test_reviews)
print(tftrain_reviews.shape)
print(tftest_reviews.shape)
print(tf.get_feature_names())
print(tftrain_reviews)
svc = LinearSVC(dual=False)
svc_train=svc.fit(tftrain_reviews,train_sentiments)
svc_predict=svc.predict(tftest_reviews)

with open('trainedmodel','wb') as f:
    pickle.dump((tf,svc),f)

print(svc_predict)

svc_score=accuracy_score(test_sentiments,svc_predict)
print(svc_score)

cm=confusion_matrix(test_sentiments,svc_predict,labels=[1,0])
print(cm)

cl_report=classification_report(test_sentiments,svc_predict)
print(cl_report)

