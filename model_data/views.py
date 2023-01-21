from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from rest_framework.decorators import api_view
# from rest_framework.response import Response
import tensorflow as tf
# import keras
import json
# import requests
# import pandas as pd
from bs4 import BeautifulSoup
from newspaper import Article, Config

# import os
# import cv2
import numpy as np
import pandas as pd
# import time
# import glob
# import requests


@api_view(["POST"])


def run_model(request):
    model = tf.keras.models.load_model('model')
    # url = request.POST.get('url')
    # request_data = url.get_json(force=True)
    request_data = json.loads(request.body.decode("utf-8"))
    data = request_data["url"]["url"]
    config = Config()
    # config.browser_user_agent = user_agent
    config.request_timeout = 10
    article = Article(data, config=config)
    article.download()
    article.parse()
    article.nlp()

    htmldata = article.html
    # soup = BeautifulSoup(htmldata, 'html.parser')
    soup = BeautifulSoup(htmldata, 'lxml')
    testData = soup.get_text()

    array = []
    array.append(testData)
    print("Finished extracting input data")

    predictions = model.predict(array)

    results = {
    '0.9':0,
    '0.8':0,
    '0.7':0,
    '0.6':0,
    '0.5':0,
    '0.4':0,
    '0.3':0,
    '0.2':0,
    '0.1':0,
    '0.0':0
    }

    for prediction in predictions:
        if(prediction[0] > 0.9):
            results['0.9'] += 1
        elif(prediction[0] > 0.8):
            results['0.8'] += 1
        elif(prediction[0] > 0.7):
            results['0.7'] += 1
        elif(prediction[0] > 0.6):
            results['0.6'] +=1
        elif(prediction[0] > 0.5):
            results['0.5'] += 1
        elif(prediction[0] > 0.4):
            results['0.4'] += 1
        elif(prediction[0] > 0.3):
            results['0.3'] += 1
        elif(prediction[0] > 0.2):
            results['0.2'] += 1
        elif(predictions[0] > 0.1):
            results['0.1'] += 1
        else:
            results['0.0'] += 1
    # return (print(results))
    return JsonResponse(results, safe=False) 
    # return flask.Response(response=json.dumps(results), status=201)