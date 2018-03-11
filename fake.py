from part2 import *
from create_set import *

def part2():
    training_set, testing_set, validation_set, training_label, testing_label, validation_label = create_set()
    answer = []
    real_dict, fake_dict = word_frequency(training_set, training_label)


    for i in range(len(testing_set)):
        ans = naive_bayes(real_dict, fake_dict, training_set, training_label, testing_set[i])
        answer.append(ans)
    
    correct = 0 

    for i in range(len(testing_set)):
        if (testing_label[i] == answer[i]):
            correct += 1 
    print correct
    
    print "accuracy"
    print correct/float(len(testing_set))


    
    return 



        
part2()








