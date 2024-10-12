import random
neurons = []
ra = random.randint
# Hellos are index 0
neurons.append(["Hello!", "Hello.", "Hey.", "Hi!", "What's up!"])
# "I am feeling" positive forms are index 1
neurons.append(["good", "fine", "nice", "good", "fine", "good", "good"])
# "I am feeling" negative forms are index 2
neurons.append(["bored and sad", "sad", "sad", "not good"])
def find_message(indexx):
    neuron = neurons[int(indexx)]
    neuron = list(neuron)
    message_index = ra(0, len(neuron) - 1)
    message =  neuron[message_index]
    return message
entry = find_message(0)
sad_feeling = find_message(2)
good_feeling = find_message(1)
def rechoose_Neuros():
    entry = find_message(0)
    sad_feeling = find_message(2)
    good_feeling = find_message(1)
print(f"{entry} I am feeling {good_feeling}.")
