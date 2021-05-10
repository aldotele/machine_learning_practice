import numpy as np


def gradient_descent(x,y):
    m_curr = b_curr = 0  # random inizialization of slope and intercept
    iterations = 10000
    n = len(x)
    learning_rate = 0.001  # arbitrary initial value
    for i in range(iterations):
        y_predicted = m_curr * x + b_curr  # y = m*x + b
        # printing the cost at each iteration
        cost = 1/n * sum([value**2 for value in (y-y_predicted)])
        # calculate partial derivatives
        md = - (2/n) * sum(x*(y - y_predicted))
        bd = - (2/n) * sum(y - y_predicted)
        # adjust values
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        print(f"m {m_curr}, b {b_curr}, iteration {i}, cost {cost}")
    pass


x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])

gradient_descent(x,y)

# the cost reduces at each iteration