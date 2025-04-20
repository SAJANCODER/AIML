#implementation of deep learning netural network
#implemetation of XOR
import numpy as np
from keras.models import Sequential
from keras.layers import Dense #dense fully connected layer recives input from all neurons of the provious layers

#1.)intilize the dataset for XOR
x=np.array([[0,0],[0,1],[1,0],[1,1]])
y=np.array([[0],[1],[1],[0]])
#2.)initilize model
model=Sequential()
#3.)add layers
model.add(Dense(4,input_dim=2,activation='relu')) #this use 4 layers and diminision 2 for the netural network
model.add(Dense(1,activation='sigmoid')) #output layer , sigmoid used because of the binary classification
#4.)compile
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
#5.)train
model.fit(x,y,epochs=100,verbose=1)
#6.)evaluate
loss ,accuracy = model.evaluate(x,y)
print(f"loss:{loss:.4f} accuracy:{accuracy:.4f}")
#7.)prediction
prediction = model.predict(x)
print("prediction")
print(prediction)



