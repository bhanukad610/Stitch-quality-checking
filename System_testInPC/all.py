from keras.preprocessing import image
import os
import tensorflow as tf
from tensorflow import keras
import numpy as np
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
from keras.preprocessing.image import ImageDataGenerator


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
new_model.load_weights('defect_detection.h5')

# image folder
folder_path = '/media/bhanuka/Education/projects/Stitch quality checking/Constrctions/dataset/all'



from PIL import Image
import numpy as np
from skimage import transform
def load(filename):
   np_image = Image.open(filename)
   np_image = np.array(np_image).astype('float32')/255
   np_image = transform.resize(np_image, (256, 256, 3))
   np_image = np.expand_dims(np_image, axis=0)
   return np_image

for img in os.listdir(folder_path):
    print(img)
    image = load(img)
    new_model.predict(image)
    #img = image.load_img(img, target_size=(img_width, img_height))
    #img = img.img_to_array(img)
    #img = np.expand_dims(img, axis=0)
    #images.append(img)

