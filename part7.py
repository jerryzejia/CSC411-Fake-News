"""
def count_words():
    content = [] 
    with open("clean_fake.txt") as f:
        _fake_content = f.readlines()
        for line in _fake_content:
            content.append(line.strip())

    with open("clean_fake.txt") as r:
        _real_content = r.readlines()
        for line in _real_content:
            content.append(line.strip())

    words = []
    count = 0
    for line in content:
        for word in line.split(" "):
            if word in words:
                continue
            words.append(word)
            count += 1
    return count

def input():
"""  

from create_set import *    
from sklearn import tree
import numpy as np
import graphviz  
from sklearn.datasets import load_iris
from sklearn import tree
iris = load_iris()

def tree_test(X,Y,vali, vali_label, max_depth):
    
    #build
    clf = tree.DecisionTreeClassifier(max_depth = max_depth)
    clf = clf.fit(X,Y)

    #graph
    dot_data = tree.export_graphviz(clf, out_file="tree.dot",
                            filled=True, rounded=True,  
                            special_characters=True)  
    graph = graphviz.Source(dot_data) 

    print clf.score(X,Y)
    print clf.score(vali, vali_label)



    '''
    #train
    train_score = 0
    for i in range(len(X)):
        c = clf.predict(np.asarray(X[i]).reshape(1,-1))[0]
        if c == Y[i]:
            train_score += 1
        print c, Y[i]
        p = clf.predict_proba(np.asarray(X[i]).reshape(1,-1))
        print p
    print "Training set accuracy: " + str(train_score/float(len(X)))

    #validate
    vali_score = 0
    for i in range(len(vali)):
        c = clf.predict(np.asarray(vali[i]).reshape(1,-1))[0]
        if c == vali_label[i]:
            vali_score += 1
        print c, vali_label[i]
        p = clf.predict_proba(np.asarray(vali[i]).reshape(1,-1))
        print p
    print "Validation set accuracy: " + str(vali_score/float(len(vali)))
    '''
    return


training_set, testing_set, validation_set, training_label, testing_label, validation_label = create_set()
training_set, testing_set, validation_set = set_conversion(training_set, testing_set, validation_set)
print training_set
print training_label
tree_test(training_set,training_label, validation_set, validation_label, 5)


    
