#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dataload import reviews


train_reviews=reviews.review[:10000]
train_sentiments=reviews.sentiment[:10000]
test_reviews=reviews.review[10001:12500]
test_sentiments=reviews.sentiment[10001:12500]
