from part2 import *
from create_set import *
#from part3 import *
def part2():
    training_set, testing_set, validation_set, training_label, testing_label, validation_label = create_set()
    answer = []
    
    print training_label
    real_dict, fake_dict = word_frequency(training_set, training_label)


    print real_dict['trump']
    for i in range(len(validation_set)):
        ans = naive_bayes(real_dict, fake_dict, training_set, training_label, validation_set[i])
        answer.append(ans)
    
    correct = 0 

    for i in range(len(validation_set)):
        if (validation_label[i] == answer[i]):
            correct += 1 
    
    print correct
    print "accuracy for validation set"
    print correct/float(len(validation_set))


    answer = []
    for i in range(len(training_set)):
        ans = naive_bayes(real_dict, fake_dict, training_set, training_label, training_set[i])
        answer.append(ans)
    
    correct = 0 

    for i in range(len(training_set)):
        if (training_label[i] == answer[i]):
            correct += 1 
    
    print correct
    print "accuracy for training set"
    print correct/float(len(training_set))





    answer = []
    for i in range(len(testing_set)):
        ans = naive_bayes(real_dict, fake_dict, training_set, training_label, testing_set[i])
        answer.append(ans)
    
    correct = 0 

    for i in range(len(testing_set)):
        if (testing_label[i] == answer[i]):
            correct += 1 
    
    print correct
    print "accuracy for testing set"
    print correct/float(len(testing_set))




    
    return 

def part3():
    #word_count()
    return

        
part2()








