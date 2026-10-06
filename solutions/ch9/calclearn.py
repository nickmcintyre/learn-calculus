import numpy as np

def predict(x, w, b):
    """Makes a prediction with a linear model"""
    y_hat = w * x + b
    return y_hat

def backprop(x, y, y_hat):
    """Computes the error gradient"""
    m = len(x)
    dE_dw = (1 / m) * np.sum((y_hat - y) * x)
    dE_db = (1 / m) * np.sum(y_hat - y)
    return [dE_dw, dE_db]

def mse(y, y_hat):
    """Computes the mean-squared error"""
    m = len(y)
    return (1 / 2 / m) * np.sum((y_hat - y) ** 2)

def train(x, y, num_epochs=100000, alpha=0.00001, log_error=False):
    """Trains a neuron with backpropagation and gradient descent"""
    w = np.random.uniform(-0.5, 0.5)
    b = np.random.uniform(-0.5, 0.5)
    if log_error:
        E = np.zeros(num_epochs)
    for i in range(num_epochs):
        # Make a prediction
        y_hat = predict(x, w, b)
        # Compute the MSE.
        if log_error:
            E[i] = mse(y, y_hat)
        # Compute the error gradient
        dE_dw, dE_db = backprop(x, y, y_hat)
        # Descend the gradient
        w -= alpha * dE_dw
        b -= alpha * dE_db
    if log_error:
        return [w, b, E]
    else:
        return [w, b]

def r_squared(y, y_hat):
    """Computes the coefficient of determination"""
    m = len(y)
    y_mean = (1 / m) * np.sum(y)
    RSS = np.sum((y_hat - y) ** 2)
    TSS = np.sum((y - y_mean) ** 2)
    R2 = 1 - RSS / TSS
    return R2

def predict_mlr(x, w, b):
    """Makes a prediction with a linear model"""
    y_hat = w @ x + b
    return y_hat

def backprop_mlr(X, y, y_hat):
    """Computes the error gradient"""
    m = len(y)
    dE_dw = (1 / m) * np.sum((y_hat - y) * X, axis=1)
    dE_db = (1 / m) * np.sum(y_hat - y)
    return [dE_dw, dE_db]

def train_mlr(X, y, num_epochs=100000, alpha=0.00001):
    """Trains a neuron with backpropagation and gradient descent"""
    num_vars = X.shape[0]
    w = np.random.uniform(-0.5, 0.5, num_vars)
    b = np.random.uniform(-0.5, 0.5)
    for i in range(num_epochs):
        # Make a prediction
        y_hat = predict_mlr(X, w, b)
        # Compute the error gradient
        dE_dw, dE_db = backprop_mlr(X, y, y_hat)
        # Descend the gradient
        w -= alpha * dE_dw
        b -= alpha * dE_db
    return [w, b]

def adj_r_squared(X, y, y_hat):
    """Computes the adjusted coefficient of determination"""
    n = X.shape[0]
    m = X.shape[1]
    R2 = r_squared(y, y_hat)
    R2_adj = 1 - (1 - R2) * (m - 1) / (m - n - 1)
    return R2_adj
