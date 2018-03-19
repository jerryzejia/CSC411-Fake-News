import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torchvision.datasets as dsets
import torchvision.transforms as transforms
from torch.autograd import Variable
import numpy as np
from create_set import *



def part4():
    #make input
    training_set, testing_set, validation_set, training_label, testing_label, validation_label = create_set()
    complete_set_word = create_complete_set(training_set, testing_set,  validation_set)
    training_set, testing_set, validation_set = set_conversion(training_set, testing_set, validation_set)
    unique_words = len(complete_set_word)
    #initialize theta
    #run gradient descend


def LinearRegression(training_set, testing_set, validation_set, training_label, testing_label, validation_label, unique_words):
	dim_x = unique_words
	dim_h = 400
	dtype_float = torch.FloatTensor
	dtype_long = torch.LongTensor

	x = Variable(torch.from_numpy(training_set), requires_grad=False).type(dtype_float)
	y_classes = Variable(torch.from_numpy(np.argmax(training_label, 1)), requires_grad=False).type(dtype_long)
	
	loss_fn = torch.nn.CrossEntropyLoss()
	learning_rate = 1e-2
	train_performance, validation_performance, test_performance = [], [], []
	
	optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
	model = LogisticRegression(input_size, num_classes)
