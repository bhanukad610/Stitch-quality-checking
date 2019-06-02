import tensorflow as tf
from tensorflow import keras
import numpy as np
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
from keras.preprocessing.image import ImageDataGenerator
import os
import shutil

def create_model():
  mobilenet_model = tf.keras.applications.mobilenet.MobileNet()
  model = tf.keras.models.Sequential()
  for layer in mobilenet_model.layers:
    model.add(layer)
    
  model.layers.pop()
  
  for layer in model.layers:
    layer.trainable = False
  model.add(Dense(2, activation = 'softmax'))
  
  model.compile(optimizer=tf.keras.optimizers.Adam(),
                loss=tf.keras.losses.sparse_categorical_crossentropy,
                metrics=['accuracy'])
  
  return model

new_model = create_model()
new_model.load_weights('oneclass.h5')

def predict():
    test_path = '/home/pi/Project/System/system'
    test_batches = ImageDataGenerator().flow_from_directory(test_path, target_size = (224,224), classes = ['Imagesvideo.h264'], batch_size = 20)
    predictions = new_model.predict_generator(test_batches, steps = 1, verbose = 0)
    os.remove('video.h264')
    shutil.rmtree('./Imagesvideo.h264')
    return finalize(predictions)


def finalize(predictions):
  result = []
  no = 0
  for pred in predictions:
    if pred[0] < 0.51:
      result.append(['no', pred[1]])
      no += 1
    else:
      result.append(['ok', pred[0]])

  return [no, result]
