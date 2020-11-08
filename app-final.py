import sklearn as sl 
from sklearn.utils import shuffle
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.models import Sequential
import pandas as pd 
import numpy as np 
import matplotlib
from matplotlib import pyplot as plt 
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import  train_test_split
import os
from flask import Flask, render_template, request
import tensorflow as tf, sys
from PIL import Image
app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
@app.route("/")
def index():
    return render_template("upload.html")
@app.route("/upload", methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT,'images/')
    print(target)
    if not os.path.isdir(target):
        os.mkdir(target)
    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)
    img=destination
    image_data = tf.gfile.FastGFile(img, 'rb').read()
    label_lines = [line.rstrip() for line
                       in tf.gfile.GFile("retrained_labels.txt")]
    with tf.gfile.FastGFile("retrained_graph.pb", 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')
    with tf.Session() as sess:
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        predictions = sess.run(softmax_tensor, \
                 {'DecodeJpeg/contents:0': image_data})
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
        name=[]
        scores=[]
        for node_id in top_k:
            human_string = label_lines[node_id]
            score = predictions[0][node_id]
            score=score*100
            if (score>20):
                print('%s (score = %.5f)' % (human_string, score))
                name.append(human_string)
                scores.append(score)   
    return render_template("complete.html",name=name,scores=scores)
if __name__ == "__main__":
    app.run(port=4555, debug=True)
    
 