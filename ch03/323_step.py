
import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    #NUMPY配列に対して不等号演算をし、をboolに変換
    #その後boolをINTに変換する
    return np.array(x > 0 ,dtype = np.int)

def sigmoid_function(x):
    #NUMPY配列に対して不等号演算をし、をboolに変換
    #その後boolをINTに変換する
    return 1/(1+np.exp(-x))

x = np.arange(-5.0,5.0,0.1)
y = sigmoid_function(x)
plt.plot(x,y)
plt.ylim(-0.1,1.1)
plt.show()
