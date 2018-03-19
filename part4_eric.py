from create_set import *
from numpy import *
import matplotlib.pyplot as plt

def part4():
    #make input
    training_set, testing_set, validation_set, training_label, testing_label, validation_label = create_set()
    training_set, testing_set, validation_set = set_conversion(training_set, testing_set, validation_set)
    #initialize theta
    init_t = np.zeros(len(training_set[0])+1)
    print init_t.shape
    #run gradient descend
    final_t = grad_descent(training_set, training_label, init_t, 0.01,0.0,testing_set,testing_label)


def func(x, y, theta, lamda):
    x = hstack((ones((len(x),1)),x))
    return sum( (y - dot(x,theta.T)) ** 2) + lamda*sum(abs(theta))

def gd(x, y, theta, lamda):
    x = hstack((ones((len(x),1)),x))
    temp = y-dot(x,theta.T)
    temp2 = dot(temp.T, x)
    return -2*sum(temp2) + lamda

def grad_descent(x, y, init_t, alpha, lamda, test, test_y):
    EPS = 1e-5   #EPS = 10**(-5)
    prev_t = init_t-10*EPS
    t = init_t.copy()
    max_iter = 30000 #or 1000 for part 4b
    iter  = 0
    succ = []
    i_list = []
    while linalg.norm(t - prev_t) >  EPS and iter < max_iter:
        prev_t = t.copy()
        t -= alpha*gd(x, y, t, lamda)

        if iter%10 ==0:
            print "Iter", iter
            succ.append(get_performance(x, y, t))
            i_list.append(iter)
        
        if iter % 500 == 0:
            print "Gradient: ",gd(x, y, t, lamda), "\n"
            
        iter += 1
    plt.plot(i_list,succ,'ro')
    plt.show()

    return t

def get_performance(x, y, theta):
    total = float(x.shape[0])
    correct = 0
    for i in range(len(x)):
        sample = hstack((1,x[i]))
        prediction = dot(sample, theta.T)
        print "prediction", prediction
        if prediction > 0.5 and y[i] == 1:
            correct += 1
        if prediction <=0.5 and y[i] == 0:
            correct += 1
    
    print "performance: ", correct/total, "\n"
    return correct/total

part4()

