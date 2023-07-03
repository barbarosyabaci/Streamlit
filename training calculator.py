import numpy as np

max = 50
no_of_sets = 3
no_of_reps = 12

# https://www.masterclass.com/articles/one-rep-max-calculator
# dict_1 = {}
list_1 = []

for no_of_reps in range(1,31):
    weight = max/(1 + (0.0333 * no_of_reps))
    Volume = weight * no_of_sets * no_of_reps
    list_1.append((no_of_reps,round(weight), round(Volume),"abc"))

print(list_1)
print(list_1[1])
print(list_1[4][3])
print(list_1[5][3][1])



