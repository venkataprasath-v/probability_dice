import math

from collections import Counter
import matplotlib.pylab as plt

n = 5  #number of dices


# Prints the list of values in each dice
#for i in range(6**n ):
#    value = i
#    for j in range(n):
#        print(math.floor(value/(6**(n-j-1))) + 1)
#        value = value - math.floor(value/(6**(n-j-1)))*(6**(n-j-1))
#    print("*****")

#prints total outcome 
outcome = []
for i in range(6**n ):
    output = 0
    value = i
    for j in range(n):
        output = output + math.floor(value/(6**(n-j-1))) + 1
        value = value - math.floor(value/(6**(n-j-1)))*(6**(n-j-1))
    outcome.append(output)

# calculate the frequency of each outcome
counts = Counter(outcome)

# calculate the probability of each outcome
total = 6**n

probability = {k:v/total for k,v in counts.items()}

print(probability)

lists = sorted(probability.items())


x, y = zip(*lists) # unpack a list of pairs into two tuples

plt.plot(x, y)
plt.show()