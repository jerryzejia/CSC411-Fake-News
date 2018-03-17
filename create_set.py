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



def set_conversion(training_set, testing_set, validation_set, training_label, testing_label, validation_label, word_num, file_num):
    complete_word_set = create_complete_set(training_set, testing_set,  validation_set)


    for tr in training set:      
        training_set_vector = np.zeros((len(complete_word_set), 1))
    


    i = 0 
    for i in range(file_num):
        return 


def create_complete_set(training_set, testing_set,  validation_set)
    complete_set = [training_set + testing_set + validation_set]
    complete_word_set = []
    for element in complete_set:
        for word in complete_set:
            if word not in complete_word_set:
                complete_word_set.append(word)
    return complete_word_set 


def input_num(train_data, word_list):



    return



    
