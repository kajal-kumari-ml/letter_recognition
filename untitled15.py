# -*- coding: utf-8 -*-
"""Untitled15.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZUAh1dG0kQ8jRCjQfWWGsO150qnpXrWA
"""

!pip install sklearn

"""## fetching **dataset**"""

from sklearn.datasets import fetch_openml
import sklearn
mnist=fetch_openml('mnist_784')

x,y= mnist['data'],mnist['target']

x

y

x[0]

x

x.shape

y.shape

import matplotlib
import matplotlib.pyplot as plt

digit=x[3609]
digit_image=digit.reshape(28,28)

digit_image

plt.imshow(digit_image,cmap=matplotlib.cm.binary,interpolation="nearest")
plt.axis("off")

y[3005]

x_train=x[:6000]
x_test=x[6000:]

y_train,y_test=y[:6000],y[6000:]

import numpy as np
import matplotlib.pyplot as plt
plt.figure(figsize=(20,4))
for index, (image, label) in enumerate(zip(x_train[0:5], y_train[0:5])):
 plt.subplot(1, 5, index + 1)
 plt.imshow(np.reshape(image, (28,28)), cmap=plt.cm.gray)
 plt.title('Training: %s\n' % label, fontsize = 20)

import numpy as np
shuffle_index=np.random.permutation(6000)

x_train,y_train=x_train[shuffle_index],y_train[shuffle_index]

"""creating 2 detector"""

y_train=y_train.astype(np.int8)
y_test=y_test.astype(np.int8)
y_train2=(y_train==3)
y_test2=(y_test==3)

y_train

from sklearn.linear_model import LogisticRegression

classi=LogisticRegression(max_iter=5000)

classi.fit(x_train,y_train)

classi.predict([digit])

from  sklearn.model_selection import cross_val_score
cross_val_score(classi,x_train,y_train2,cv=3,scoring="accuracy")

