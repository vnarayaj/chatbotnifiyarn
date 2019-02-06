#!/usr/bin/env python3
from flask import Flask, request,jsonify #import main Flask class and request object
from collections import defaultdict
import requests
import time
import argparse
import os
import json
import re
from dialogue_manager import *

from requests.compat import urljoin
t=defaultdict(dict)
#t=dict()
paths =  {
        'INTENT_RECOGNIZER': '/home/ubuntu/intent_recognizer.pkl',
        'TAG_CLASSIFIER': '/home/ubuntu/tag_classifier.pkl',
        'TFIDF_VECTORIZER': '/home/ubuntu/tfidf_vectorizer.pkl',
        'THREAD_EMBEDDINGS_FOLDER': '/home/ubuntu/thread_embeddings_by_tags',
        'WORD_EMBEDDINGS': '/home/ubuntu/starspace_embedding.tsv',
        }
simple_manager = DialogueManager(paths)
offset=-1
app = Flask(__name__) #create the Flask app
@app.route('/json-example',methods = ['POST', 'GET'])
def json_example():
	req_data = request.get_json()
	print(req_data)
	if req_data!=True and not isinstance(req_data,int):
		#for i in range(len(req_data)):
			chatid=req_data['message']['chat']['id']
			updateid=req_data['update_id']
			resp=simple_manager.generate_answer(req_data["message"]["text"])
			resp=str(resp)
			resp=resp.replace(',',' ')
			print(resp)
			t['chatid']=chatid
			t['resp']=resp
			t['updateid']=updateid
	return jsonify(t)
#	return 'done'

if __name__ == '__main__':
	app.run(port=5000,host='0.0.0.0')
