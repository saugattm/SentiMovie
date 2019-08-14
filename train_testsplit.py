#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dataload import reviews


train_reviews=reviews.review[:12500]
train_sentiments=reviews.sentiment[:12500]
test_reviews=reviews.review[12500:]
test_sentiments=reviews.sentiment[12500:]
