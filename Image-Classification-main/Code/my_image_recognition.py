
from keras.models import load_model 
from skimage.transform import resize 
import numpy as np 
import matplotlib.pyplot as plt
import pickle 
from sklearn.metrics import classification_report
import random



model = load_model('Models/my_cifar10_model2_augmented.h5')
x_test=pickle.load(open("Data/x_test.dat","rb"))
y_test=pickle.load(open("Data/y_test.dat","rb"))
y_test_label=np.argmax(np.round(y_test),axis=1)
number_to_class = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog',\
                   'frog', 'horse', 'ship', 'truck']
predicted_classes=model.predict(x_test)   
predicted_classes_label=np.argmax(np.round(predicted_classes),axis=1)
correct=np.where(predicted_classes_label==y_test_label)[0] 
incorrect=np.where(predicted_classes_label!=y_test_label)[0]
random = random.randint(0, len(incorrect))
plt.subplot(2,2,1)
plt.imshow(x_test[incorrect[random]].reshape(32,32,3),cmap='gray',interpolation='none')
plt.title('Predicted '+str(number_to_class[predicted_classes_label[incorrect[random]]])+\
          ', correct '+str(number_to_class[y_test_label[incorrect[random]]]))
plt.tight_layout()
target_names = [number_to_class[i] for i in range(10)]
print(classification_report(y_test_label, predicted_classes_label,\
                            target_names=target_names))              
my_image=plt.imread("Images/my_image_1.jpg")
my_image_resized=resize(my_image, (32,32,3))
img=plt.imshow(my_image) 
probabilities=model.predict(np.array([my_image_resized]))
index = np.argsort(probabilities[0,:])
print("Most likely class:", number_to_class[index[9]], "-- Probability:",\
      probabilities[0,index[9]])
print("Second most likely class:", number_to_class[index[8]], "-- Probability:",\
      probabilities[0,index[8]])
print("Third most likely class:", number_to_class[index[7]], "-- Probability:",\
      probabilities[0,index[7]])
print("Fourth most likely class:", number_to_class[index[6]], "-- Probability:",\
      probabilities[0,index[6]])
print("Fifth most likely class:", number_to_class[index[5]], "-- Probability:",\
      probabilities[0,index[5]])
