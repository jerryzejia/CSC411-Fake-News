import math 

def small_multiplication(n):
    log_sum = 0.
    for num in n:
        log_sum += math.log(num)
    exponent = math.exp(log_sum)
    return exponent 




def naive_bayes(real_frequency_dictionary, fake_frequency_dictionary, training_set, training_label, test):
    count_fake = training_label.count(0)
    count_real = training_label.count(1)

    P_fake = float(count_fake)/float(len(training_label)) #0.4
    P_real = float(count_real)/float(len(training_label)) #0.6

    real_chances = [] 
    fake_chances = [] 
    test = test.split()

    fake_total_val = sum(fake_frequency_dictionary.values())
    real_total_val = sum(real_frequency_dictionary.values())


    for word, frequency in fake_frequency_dictionary.iteritems():
        P_frequency = (frequency+2*0.4)/float(fake_total_val + 2)
    
        if word in test:
            fake_chances.append(P_frequency)
        else:
            fake_chances.append(1. - P_frequency)
    for word, frequency in real_frequency_dictionary.iteritems():
        P_frequency = (frequency+2*0.6)/float(real_total_val + 2)
        if word in test:
            real_chances.append(P_frequency)
        else:
            real_chances.append(1. - P_frequency)


    P_words_fake = small_multiplication(fake_chances)
    P_fake_words = P_fake * P_words_fake

    P_words_real = small_multiplication(real_chances)
    P_real_words = P_real * P_words_real
    P = P_fake_words/(P_fake_words + P_real_words)

    return 0 if P > 0.5 else 1


def word_frequency(training_set, training_label):
    '''
    Fake News Frequency Counter 
    '''
    real_frequency_dictionary = {}
    fake_frequency_dictionary = {}

    for i in range(len(training_set)):
        title = training_set[i]
        label = training_label[i]
        words = title.split()
        for word in list(set(words)):
            if label == 1:
                if word not in real_frequency_dictionary:
                    real_frequency_dictionary[word] = 1 
                else:
                    real_frequency_dictionary[word] += 1 

                if word not in fake_frequency_dictionary:
                    fake_frequency_dictionary[word] = 0 

            elif label == 0:
                if word not in fake_frequency_dictionary:
                    fake_frequency_dictionary[word] = 1 
                else:
                    fake_frequency_dictionary[word] += 1 

                if word not in real_frequency_dictionary:
                    real_frequency_dictionary[word] = 0 

    return real_frequency_dictionary, fake_frequency_dictionary