import random 
import numpy as np 

def create_set():
    real, fake = [], []
    training_label, testing_label, validation_label = [], [], [] 
    training_set, testing_set, validation_set = [], [], [] 
    random.seed(0)

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
            testing_set.append(0)

    
    