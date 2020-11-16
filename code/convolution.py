from PIL import Image
import numpy as np
import glob
from sklearn.model_selection import train_test_split
from tensorflow.image import resize
from tensorflow.keras import layers, models, utils
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import to_categorical
from matplotlib import pyplot as plt

train_images = []
train_labels = []
test_images  = []
test_labels  = []

image_size = 100

folderE     = "./letterE"
folderF     = "./letterF"
folderI     = "./letterL"
folderO     = "./letterO"
folderR     = "./letterR"
folderFour  = "./numberFour"
folderFive  = "./numberFive"
folderSeven = "./numberSeven"
folderNine  = "./numberNine"
folderTen   = "./numberTen"

folders = [folderE, folderF, folderI, folderO, folderR, folderFour, folderFive, folderSeven, folderNine, folderTen]

### Looping through each folder ###
for i in range(len(folders)):
    images = [j for j in glob.iglob(folders[i] + "/*.jpg")]
    for j in images:
        try:
            img = resize(np.asarray(Image.open(j)), [image_size,image_size])
            train_images.append(np.asarray(img))
        except:
            print("No file")
        train_labels.append(i)


train_images, test_images, train_labels, test_labels = train_test_split(train_images, train_labels, test_size=0.2)

train_labels = np.asarray(train_labels)
train_images = np.asarray(train_images)

test_labels = np.asarray(test_labels)
test_images = np.asarray(test_images)

train_images = (train_images / 255) - 0.5
test_images = (test_images / 255) - 0.5


filter_size = (3,3)
pool_size = (2,2)

# Build the model.

### This model is not used by default ###
model_one = models.Sequential()
model_one.add(layers.Conv2D(8, filter_size, activation='relu', input_shape=(image_size, image_size, 3)))
model_one.add(layers.MaxPooling2D(pool_size))
model_one.add(layers.Flatten())
model_one.add(layers.Dense(10, activation='softmax'))

### Default model ###
model_two = models.Sequential()
model_two.add(layers.Conv2D(16, filter_size, activation='relu', input_shape=(image_size, image_size, 3)))
model_two.add(layers.MaxPooling2D(pool_size))
model_two.add(layers.Conv2D(32, filter_size, activation='relu'))
model_two.add(layers.MaxPooling2D(pool_size))
model_two.add(layers.Conv2D(64, filter_size, activation='relu'))
model_two.add(layers.MaxPooling2D(pool_size))
model_two.add(layers.Flatten())
model_two.add(layers.Dense(10, activation='softmax'))

### Change this to either model_one or model_two to use a different model ###
model = model_two 

# Compile the model.
model.compile(
  'adam',
  loss='categorical_crossentropy',
  metrics=['accuracy'],
)

# Train the model.
history = model.fit(
    train_images,
    to_categorical(train_labels),
    epochs=8,
    validation_data=(test_images, to_categorical(test_labels)),
    shuffle='true'
)

# Evaluating the resulting convolutional neural network
model.evaluate(test_images, to_categorical(test_labels))

# Graphing the resulting accuracy of each epoch
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'val'], loc='upper left')
plt.show()

# Graphing the resulting loss of each epoch
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'val'], loc='upper left')
plt.show()
