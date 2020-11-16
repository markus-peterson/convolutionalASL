from tensorflow.image import resize
from tensorflow.keras import layers, models, utils
from tensorflow.keras.models import Sequential

image_size = 100
filter_size = (3,3)
pool_size = (2,2)

model_one = models.Sequential()
model_one.add(layers.Conv2D(8, filter_size, activation='relu', input_shape=(image_size, image_size, 3)))
model_one.add(layers.MaxPooling2D(pool_size))
model_one.add(layers.Flatten())
model_one.add(layers.Dense(10, activation='softmax'))

model_two = models.Sequential()
model_two.add(layers.Conv2D(16, filter_size, activation='relu', input_shape=(image_size, image_size, 3)))
model_two.add(layers.MaxPooling2D(pool_size))
model_two.add(layers.Conv2D(32, filter_size, activation='relu'))
model_two.add(layers.MaxPooling2D(pool_size))
model_two.add(layers.Conv2D(64, filter_size, activation='relu'))
model_two.add(layers.MaxPooling2D(pool_size))
model_two.add(layers.Flatten())
model_two.add(layers.Dense(10, activation='softmax'))

model_one.summary()
model_two.summary()