from create_set import *

def part4():
    training_set, testing_set, validation_set, training_label, testing_label, validation_label = create_set()
    training_set, testing_set, validation_set = set_conversion(training_set, testing_set, validation_set)
    print training_set[0]
part4()