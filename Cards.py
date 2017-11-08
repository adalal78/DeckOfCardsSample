
# coding: utf-8

# In[114]:

def CardValue(card):
    
    value = 0
    
    if(card[0] == 'A'):
        value = value + 1
        
    elif(card[0] == 'J' or card[0] == 'Q' or card[0] == 'K'):
        value = value + 10
        
    else:
        value = value + int(card[0])
        
    return value

def OneCardSample():
    
    CardSampleSum = 0
    CardDeck = ['Ac', '2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', '10c', 'Jc', 'Qc', 'Kc', 'Ad', '2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', '10d', 'Jd', 'Qd', 'Kd', 'Ah', '2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', '10h', 'Jh', 'Qh', 'Kh', 'As', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', '10s', 'Js', 'Qs', 'Ks']
    random.shuffle(CardDeck)
    size = len(CardDeck)
    
    Index = random.randrange(size)
    randCard = CardDeck[Index]
    randCardValue = CardValue(list(randCard))
    return [randCard, randCardValue]

def OneCardTrials(n):
    
    CardValueArray = [0 for i in range(0,n)]
    
    for i in range(0,n):
        Sample = OneCardSample()
        CardValueArray[i] = Sample[1]
        
    return CardValueArray


def ThreeCardSample():
    
    CardSampleSum = 0
    CardDeck = ['Ac', '2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', '10c', 'Jc', 'Qc', 'Kc', 'Ad', '2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', '10d', 'Jd', 'Qd', 'Kd', 'Ah', '2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', '10h', 'Jh', 'Qh', 'Kh', 'As', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', '10s', 'Js', 'Qs', 'Ks']
    random.shuffle(CardDeck)
    size = len(CardDeck)
    
    removeAtIndex = random.randrange(size)
    rand1 = CardDeck[removeAtIndex]
    CardSampleSum = CardSampleSum + CardValue(list(rand1))
    CardDeck[removeAtIndex] = CardDeck[size-1]
    
    removeAtIndex = random.randrange(size-1)
    rand2 = CardDeck[removeAtIndex]
    CardSampleSum = CardSampleSum + CardValue(list(rand2))
    CardDeck[removeAtIndex] = CardDeck[size-2]
    
    removeAtIndex = random.randrange(size-2)
    rand3 = CardDeck[removeAtIndex]
    CardSampleSum = CardSampleSum + CardValue(list(rand3))
    return [rand1, rand2, rand3, CardSampleSum]

def ThreeCardTrials(n):
    
    ThreeCardSums = [0 for i in range(0,n)]
    for i in range(0,n):
        Sample = ThreeCardSample()
        ThreeCardSums[i] = Sample[3]
        #print Sample[0], Sample[1], Sample[2], Sample[3]
    
    return ThreeCardSums


# In[122]:

import numpy as np
import matplotlib.pyplot as plt
ThreeCardSums = ThreeCardTrials(100000)
print "Average is ", np.average(ThreeCardSums) 
print "Median is ", np.median(ThreeCardSums)
print "Standard deviation is ", np.std(ThreeCardSums)
myBins = [3*i for i in range(1,11)]
plt.hist(ThreeCardSums, bins = myBins)
plt.show()


# In[117]:

import numpy as np
import matplotlib.pyplot as plt
OneCardSum = OneCardTrials(100000)
myBins = [i for i in range(0,11)]
plt.hist(OneCardSum, bins = myBins)
plt.show()


# In[ ]:



