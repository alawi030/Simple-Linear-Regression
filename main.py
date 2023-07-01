import numpy as np
from sklearn.linear_model import LinearRegression

# Generate some random data
np.random.seed(0)
X = np.random.random((10,1))
Y = 2 * X + 1 + np.random.randn(10,1)

# Create an instance of the linear regression model
model = LinearRegression()

# Fit the model to the data
model.fit( X , Y )

# Predict the output for a new input
new_X = np.array([[0.5], [1.5]])
predictions = model.predict(new_X)

# Print the predictions
print(X)
print(Y)
print(predictions)

lol
