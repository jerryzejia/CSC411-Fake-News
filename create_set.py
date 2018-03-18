import random 
import numpy as np 

def create_set():
    real, fake = [], []
    training_label, testing_label, validation_label = [], [], [] 
    training_set, testing_set, validation_set = [], [], [] 
    random.seed(5)

    content_fake = [] 
    with open("clean_fake.txt") as f:
        _fake_content = f.readlines()
        for line in _fake_content:
            content_fake.append(line.strip())


    content_real = []
    with open("clean_fake.txt") as r:
        _real_content = r.readlines()
        for line in _real_content:
            content_real.append(line.strip())

    random.shuffle(content_real)
    random.shuffle(content_fake)

    for i in range(len(content_fake)):
        if i < 0.15*len(content_fake):
            testing_set.append(content_fake[i])
            testing_label.append(0)

        elif i < 0.30*len(content_fake):
            validation_set.append(content_fake[i])
            validation_label.append(0)
        
        else:
            training_set.append(content_fake[i])
            training_label.append(0)


    for i in range(len(content_real)):
        if i < 0.15*len(content_real):
            testing_set.append(content_real[i])
            testing_label.append(1)

        elif i < 0.30*len(content_real):
            validation_set.append(content_real[i])
            validation_label.append(1)
        
        else:
            training_set.append(content_real[i])
            training_label.append(1)

    return training_set, testing_set, validation_set, training_label, testing_label, validation_label



def set_conversion(training_set, testing_set, validation_set):
    training_set, testing_set, validation_set = list(training_set), list(testing_set), list(validation_set)
    complete_word_set = create_complete_set(training_set, testing_set,  validation_set)
    training_set_classifier = np.zeros((len(training_set) ,len(complete_word_set)))

    for i in range(len(training_set)):      
        for word in training_set[i].split():
            training_set_classifier[i][complete_word_set.index(word)] = 1

    testing_set_classifier = np.zeros((len(testing_set) ,len(complete_word_set)))
    for i in range(len(testing_set)):      
        for word in testing_set[i].split():
            testing_set_classifier[i][complete_word_set.index(word)] = 1


    validation_set_classifier = np.zeros((len(validation_set) ,len(complete_word_set)))
    for i in range(len(validation_set)):      
        for word in validation_set[i].split():
            validation_set_classifier[i][complete_word_set.index(word)] = 1

    return training_set_classifier, validation_set_classifier, testing_set_classifier




def create_complete_set(training_set, testing_set,  validation_set):
    complete_set = []
    complete_set.extend(training_set)
    complete_set.extend(testing_set)
    complete_set.extend(validation_set)
    complete_word_set = []
    for element in complete_set:
        for word in element.split():
            if word not in complete_word_set:
                complete_word_set.append(word)
    random.seed(0)
    return complete_word_set 




    
