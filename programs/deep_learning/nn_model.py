import numpy as np
from keras.models import Sequential
from keras.layers import Dense
# Sample dataset: XOR problem
X = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([[0], [1], [1], [0]])
# Create a Sequential model
model = Sequential()

# Add layers to the model
model.add(Dense(4, input_dim=2, activation='relu'))  # Hidden layer with 4 neurons
model.add(Dense(1, activation='sigmoid'))            # Output layer (sigmoid used for binary classification)
# Compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# Train the model
model.fit(X, y, epochs=100, verbose=1)
# Evaluate the model
loss, accuracy = model.evaluate(X, y)
print(f'Loss: {loss:.4f}, Accuracy: {accuracy:.4f}')
# Make predictions
predictions = model.predict(X)
print("Predictions:")
print(predictions)
