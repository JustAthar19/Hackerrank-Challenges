import numpy as np
from sklearn.linear_model import LinearRegression

# first solution

physics = [15,12,8,8,7,7,7,6,5,3]
history = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

x = np.array(physics).reshape(-1, 1)
y = np.array(history)


model = LinearRegression()
model.fit(x,y)

print("{:.3f}".format(model.coef_[0]))

# option  2 
def get_regr_slope(x,y):
    xy = [a*b for a, b in zip(x,y)]
    n = len(x)
    x_2 = [a*a for a in x]
    num = n*sum(xy) - sum(x)*sum(y)
    denom = n*sum(x_2) - sum(x)**2
    slope = num/denom
    print("%.1f" % slope)


get_regr_slope(physics, history)
