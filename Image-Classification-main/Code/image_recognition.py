
from keras.datasets import cifar10 
import matplotlib.pyplot as plt
import keras
from keras.models import Sequential 
from keras.layers import Dense, Dropout, Flatten, Conv2D,\
    MaxPooling2D 
import pickle 
import random


(x_train, y_train), (x_test, y_test) = cifar10.load_data()
random = random.randint(0, len(x_train))
img=plt.imshow(x_train[random])
y_train_one_hot=keras.utils.to_categorical(y_train,10)
y_test_one_hot=keras.utils.to_categorical(y_test,10)
x_train=x_train.astype('float32') 
x_test=x_test.astype('float32')
x_train=x_train/255
x_test=x_test/255
pickle.dump(x_test, open("Data/x_test.dat", "wb"))
pickle.dump(y_test_one_hot, open("Data/y_test.dat", "wb")) 
model=Sequential() 
model.add(Conv2D(32,(3,3), activation='relu', padding='same',\
                 input_shape=(32,32,3)))
model.add(Conv2D(32,(3,3), activation='relu', padding='same'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))
model.add(Conv2D(64,(3,3), activation='relu', padding='same'))
model.add(Conv2D(64,(3,3), activation='relu', padding='same'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(512,activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10,activation='softmax'))
model.summary()
model.compile(loss='categorical_crossentropy', optimizer='adam',\
              metrics=['accuracy'])
hist=model.fit(x_train,y_train_one_hot, batch_size=32,epochs=20,\
               validation_split=0.2)
plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Training', 'Validation'], loc='upper right')
plt.show()
plt.plot(hist.history['accuracy']) 
plt.plot(hist.history['val_accuracy'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch') 
plt.legend(['Training', 'Validation'], loc='lower right')
plt.show()
print('CIFAR10 32x32 RGB TEST SET ACCURACY')
print(model.evaluate(x_test,y_test_one_hot)[1]*100,'%')
model.save('model_name.h5')
