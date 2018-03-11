import math 

def small_multiplication(n):
    log_sum = 0 
    for num in n:
        log_sum += math.log(num)
    exponent = math.exp(log_sum)
    return exponent 




def native_bayes(real_frequency_dictionary, fake_frequency_dictionary, training_set, training_label, test):
    length = len(test)
    P_real = float(training_label.count(1))/float(len(training_label))
    P_fake = float(training_label.count(0))/float(len(training_label))


    real_chances = [] 
    fake_chances = [] 

    for word, frequency in real_frequency_dictionary.iteritems():
        P_frequency = frequency/float(training_label.count(1))
        if word in test:
            real_chances.append(P_frequency)
        else:
            real_chances.append(1. - P_frequency)


    for word, frequency in fake_frequency_dictionary.iteritems():
        P_frequency = frequency/float(training_label.count(0))
        if word in test:
            fake_chances.append(P_frequency)
        else:
            fake_chances.append(1. - P_frequency)


    P_words_fake = small_multiplication(fake_chances)


    P = P_fake * P_words_fake

    if P > 0.5:
        return 1 
    else:
        return 0 


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