import math 

def small_multiplication(n):
    log_sum = 0 
    for num in n:
        log_sum += math.log(num)
    exponent = math.exp(log_sum)
    return exponent 




def naive_bayes(real_frequency_dictionary, fake_frequency_dictionary, training_set, training_label, test):
    P_fake = float(training_label.count(0))/float(len(training_label))
    P_real = float(training_label.count(1))/float(len(training_label))

    real_chances = [] 
    fake_chances = [] 
    test = test.split(" ")
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
    P_fake_words = P_fake * P_words_fake

    P_words_real = small_multiplication(real_chances)
    P_real_words = P_real * P_words_real

    P = P_real_words/(P_fake_words+P_real_words)

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

        for word in list(set(words)):
            if label == 1:
                if word not in real_frequency_dictionary:
                    real_frequency_dictionary[word] = 1 
                else:
                    real_frequency_dictionary[word] += 1 
            else:
                if word not in fake_frequency_dictionary:
                    fake_frequency_dictionary[word] = 1 
                else:
                    fake_frequency_dictionary[word] += 1 

    return real_frequency_dictionary, fake_frequency_dictionary