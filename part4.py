stop_word = [
    "a", "about", "above", "across", "after", "afterwards", "again", "against",
    "all", "almost", "alone", "along", "already", "also", "although", "always",
    "am", "among", "amongst", "amoungst", "amount", "an", "and", "another",
    "any", "anyhow", "anyone", "anything", "anyway", "anywhere", "are",
    "around", "as", "at", "back", "be", "became", "because", "become",
    "becomes", "becoming", "been", "before", "beforehand", "behind", "being",
    "below", "beside", "besides", "between", "beyond", "bill", "both",
    "bottom", "but", "by", "call", "can", "cannot", "cant", "co", "con",
    "could", "couldnt", "cry", "de", "describe", "detail", "do", "done",
    "down", "due", "during", "each", "eg", "eight", "either", "eleven", "else",
    "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone",
    "everything", "everywhere", "except", "few", "fifteen", "fifty", "fill",
    "find", "fire", "first", "five", "for", "former", "formerly", "forty",
    "found", "four", "from", "front", "full", "further", "get", "give", "go",
    "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter",
    "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his",
    "how", "however", "hundred", "i", "ie", "if", "in", "inc", "indeed",
    "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter",
    "latterly", "least", "less", "ltd", "made", "many", "may", "me",
    "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly",
    "move", "much", "must", "my", "myself", "name", "namely", "neither",
    "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone",
    "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on",
    "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our",
    "ours", "ourselves", "out", "over", "own", "part", "per", "perhaps",
    "please", "put", "rather", "re", "same", "see", "seem", "seemed",
    "seeming", "seems", "serious", "several", "she", "should", "show", "side",
    "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone",
    "something", "sometime", "sometimes", "somewhere", "still", "such",
    "system", "take", "ten", "than", "that", "the", "their", "them",
    "themselves", "then", "thence", "there", "thereafter", "thereby",
    "therefore", "therein", "thereupon", "these", "they", "thick", "thin",
    "third", "this", "those", "though", "three", "through", "throughout",
    "thru", "thus", "to", "together", "too", "top", "toward", "towards",
    "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us",
    "very", "via", "was", "we", "well", "were", "what", "whatever", "when",
    "whence", "whenever", "where", "whereafter", "whereas", "whereby",
    "wherein", "whereupon", "wherever", "whether", "which", "while", "whither",
    "who", "whoever", "whole", "whom", "whose", "why", "will", "with",
    "within", "without", "would", "yet", "you", "your", "yours", "yourself",
    "yourselves"]


import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torchvision.datasets as dsets
import torchvision.transforms as transforms
from torch.autograd import Variable
import numpy as np
from create_set import *




#https://www.kaggle.com/negation/pytorch-logistic-regression-tutorial
class LogisticRegression(nn.Module):
	def __init__(self, input_size, num_classes):
		super(LogisticRegression, self).__init__()
		self.linear = nn.Linear(input_size, num_classes)
	
	def forward(self, x):
		out = self.linear(x)
		return out



def part4():
	#make input
	training_set, testing_set, validation_set, training_label, testing_label, validation_label = create_set()
	complete_set_word = create_complete_set(training_set, testing_set,  validation_set)
	training_set, testing_set, validation_set = set_conversion(training_set, testing_set, validation_set)
	training_label, testing_label, validation_label = int_to_one_hot(training_label, testing_label, validation_label)

	unique_words = len(complete_set_word)
	final_t	= LinearRegression(training_set, testing_set, validation_set, training_label, testing_label, validation_label, unique_words)

	part6(final_t, training_set, complete_set_word)
	#part6
	#initialize theta
	#run gradient descend


def int_to_one_hot(training_label, testing_label, validation_label):
	training_label_oh = []
	for tr in training_label:
		if tr == 1:
			training_label_oh.append([0, 1])
		else: 
			training_label_oh.append([1, 0])

	testing_label_oh = []
	for tr in testing_label:
		if tr == 1:
			testing_label_oh.append([0, 1])
		else: 
			testing_label_oh.append([1, 0])

	validation_label_oh = []
	for tr in validation_label:
		if tr == 1:
			validation_label_oh.append([0, 1])
		else: 
			validation_label_oh.append([1, 0])

	return training_label_oh, testing_label_oh, validation_label_oh


def LinearRegression(training_set, testing_set, validation_set, training_label, testing_label, validation_label, unique_words):
	dim_x = unique_words
	dim_h = 400
	dtype_float = torch.FloatTensor
	dtype_long = torch.LongTensor
	max_iteration = 1000
	x = Variable(torch.from_numpy(training_set), requires_grad=False).type(dtype_float)
	y_classes = Variable(torch.from_numpy(np.argmax(training_label, 1)), requires_grad=False).type(dtype_long)
	
	loss_fn = torch.nn.CrossEntropyLoss()
	learning_rate = 1e-2
	train_performance, validation_performance, test_performance = [], [], []
	iteration = []
	reg_lambda = 0.01


	model = LogisticRegression(input_size = dim_x, num_classes = 2)
	optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
	for i in range(max_iteration+1):
		l2_reg = Variable( torch.FloatTensor(1), requires_grad=True)
		prediction = model(x)
		for W in model.parameters():
			if l2_reg is None:
				l2_reg = W.norm(2)
			else:
				l2_reg = l2_reg + W.norm(2)
		loss = loss_fn(prediction, y_classes) + reg_lambda * l2_reg
		model.zero_grad()
		loss.backward()
		optimizer.step()




		if i % 50 == 0:
			#print("Iteration: " + str(i))
			x_train = Variable(torch.from_numpy(training_set), requires_grad=False).type(dtype_float)
			y_pred = model(x_train).data.numpy()
			training_accuracy = np.mean(np.argmax(y_pred, 1) == np.argmax(training_label, 1)) * 100
			train_performance.append(training_accuracy)
			#print("Training Set Performance  : " + str(training_accuracy) + "%")      


			x_valid = Variable(torch.from_numpy(validation_set), requires_grad=False).type(dtype_float)
			y_pred = model(x_valid).data.numpy()
			validation_accuracy = np.mean(np.argmax(y_pred, 1) == np.argmax(validation_label, 1)) * 100
			validation_performance.append(validation_accuracy)
			#print("Validation Set Performance  : " + str(validation_accuracy) + "%")      

			iteration.append(i)


	plt.plot(iteration, train_performance,  label="Training Set")
	plt.plot(iteration, validation_performance, label="Validation Set")
	plt.title("Learning curve")
	plt.legend()
	plt.show()


	return model.linear.weight.data.numpy()

def part6(final_t, training_set, complete_set_word):
	t = final_t[0] - final_t[1]
	sorted_t = sorted(t)
	smallest = sorted_t[0:10]
	largest = sorted_t[-11:-1]
	print "------------------- Including Stop Words-------------------"
	print "-------------------most negative: -------------------"
	for weight in smallest:
		ind = list(t).index(weight)
		print str(weight) + ": "
		print complete_set_word[ind] + ", "

	print "-------------------most positive: -------------------"
	for weight in largest:
		ind = list(t).index(weight)
		print str(weight) + ": "
		print complete_set_word[ind] + ", "

	print "------------------- Excluding Stop Words-------------------"
	print "-------------------most negative: -------------------"
	i = 0
	count = 10 

	while i <= count:
		weight = sorted_t[i]
		ind = list(t).index(weight)
		word = complete_set_word[ind]
		if word not in stop_word:
			print str(weight) + ": "
			print word + ", "
		else:
			count += 1 
		i += 1

	print "-------------------most positive: -------------------"
	i = 0

	count = 10 
	while i <= count:
		weight = sorted_t[0-i-1]
		ind = list(t).index(weight)
		word = complete_set_word[ind]
		if word not in stop_word:
			print str(weight) + ": "
			print word + ", "
		else: 
			count += 1 
		i += 1

part4()