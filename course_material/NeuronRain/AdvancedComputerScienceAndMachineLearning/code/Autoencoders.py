import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from tensorflow.keras import layers, losses
from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.models import Model
import cv2

class Autoencoder(Model):
  def __init__(self, latent_dim, shape):
    super(Autoencoder, self).__init__()
    self.latent_dim = latent_dim
    self.shape = shape
    self.encoder = tf.keras.Sequential([
      layers.Flatten(),
      layers.Dense(latent_dim, activation='relu'),
    ])
    self.decoder = tf.keras.Sequential([
      layers.Dense(tf.math.reduce_prod(shape).numpy(), activation='sigmoid'),
      layers.Reshape(shape)
    ])

  def call(self, x):
    encoded = self.encoder(x)
    decoded = self.decoder(encoded)
    return decoded

def fraud_and_anomaly_detection(x_train,x_test,datatype="scalar"):
    #(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
    x_train = x_train.astype('float32') / 255.
    x_test = x_test.astype('float32') / 255.
    shape = x_test.shape[1:]
    latent_dim = 64
    autoencoder = Autoencoder(latent_dim, shape)
    autoencoder.compile(optimizer='adam', loss=losses.MeanSquaredError())
    print("training dataset shape:",x_train.shape)
    print("test dataset shape:",x_test.shape)
    autoencoder.fit(x_train, x_train,
                epochs=10,
                shuffle=True,
                validation_data=(x_test, x_test))
    encoded = autoencoder.encoder(x_test).numpy()
    decoded = autoencoder.decoder(encoded).numpy()
    print("dataset:",x_test)
    print("encoded dataset:",encoded)
    print("decoded dataset (must be close to dataset):",decoded)
    if datatype=="scalar":
        plt.plot(x_test,label="dataset before autoencoding")
        plt.plot(decoded,label="decoded dataset by autoencoders")
        plt.legend()
        plt.show()
    if datatype=="visual":
        cv2.imwrite("testlogs/Autoencoders.decoded.jpg",255*decoded)
    return (encoded,decoded)

if __name__=="__main__":
    #x_train = np.sin(1000*np.linspace(-np.pi,0,200))
    #x_dataset = np.sin(1000*np.linspace(0,np.pi,200))
    x_train = 10*np.random.rand(100)
    x_dataset = 10*np.random.rand(100)
    fraud_and_anomaly_detection(x_train,x_dataset,datatype="scalar")
    x_train = cv2.imread("testlogs/Random_female_face_1.jpeg")
    x_dataset = cv2.imread("testlogs/Random_female_face_1.jpeg")
    fraud_and_anomaly_detection(x_train,x_dataset,datatype="visual")
