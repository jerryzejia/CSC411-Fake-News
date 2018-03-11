import math 

def small_multiplication(n):
    log_sum = 0 
    for num in n:
        log_sum += math.log(num)
    exponent = math.exp(log_sum)
    return exponent 




def native_bayes(real_frequency_dictionary, fake_frequency_dictionary, training_set, training_label, test):
    length = len(test)



    return



def word_frequency(training_set, training_label):
    '''
    Fake News Frequency Counter 
    '''
    real_frequency_dictionary = {}
    fake_frequency_dictionary = {}

    for i in range(len(training_set)):
        title = training_set[i]
        label = training_label[i]
        words = title.split(" ")
        for word in words:
            if label == 1:
                if not real_frequency_dictionary[word]:
                    real_frequency_dictionary[word] = 1 
                else:
                    real_frequency_dictionary[word] += 1 
            else:
                if not fake_frequency_dictionary[word]:
                    fake_frequency_dictionary[word] = 1 
                else:
                    fake_frequency_dictionary[word] += 1 

    return real_frequency_dictionary, fake_frequency_dictionary