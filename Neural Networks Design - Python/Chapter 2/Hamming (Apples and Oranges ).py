# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 19:02:20 2017

@author: Chris Amirani

This is a single layer nn incorporating Hamming network to distinguish Apples and Oranges.
"""

import numpy as np

#this is the input data [shape,surface,heaviness]
inputs= ([-1,1,1],[-1,-1,1],[1,1,-1],[1,-1,-1],[1,-1,-1],[1,-1,1],[1,1,-1],[1,1,-1],[-1,-1,-1],[1,1,1],
         [1,-1,1],[1,1,1],[1,1,1],[-1,-1,1],[-1,1,1],[1,-1,1],[1,1,1],[1,-1,1],[1,-1,1],[-1,-1,1],
         [1,1,1],[1,1,1],[-1,1,1],[1,1,-1],[1,1,1],[-1,1,1],[1,1,1],[1,1,-1],[-1,1,1],[1,-1,1],
         [-1,1,-1],[-1,1,1],[1,1,1],[1,-1,-1],[-1,1,1],[1,1,1],[1,-1,1],[1,1,-1],[1,1,1],
         [1,1,-1],[1,1,1],[-1,1,1],[1,1,1],[1,1,1],[1,1,-1],[1,1,-1],[-1,1,1],[1,-1,1],[1,1,1],
         [1,1,1],[1,-1,-1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,-1,1],[1,-1,1],[1,-1,1],[1,-1,1],
         [1,1,1],[1,1,1],[1,1,1],[1,1,-1],[1,1,1],[1,1,1],[1,-1,1],[1,1,-1],[1,-1,-1],[-1,-1,-1],
         [1,1,-1],[1,1,1],[1,-1,1],[1,1,1],[1,1,1],[1,-1,1],[1,1,1],[1,1,1],[-1,1,1],[1,1,1],[1,1,-1],
         [1,1,1],[1,1,-1],[-1,-1,-1],[-1,1,1],[1,-1,-1],[1,1,-1],[-1,1,1],[1,1,1],[1,-1,-1],[-1,1,1],[1,1,1],
         [-1,1,1],[1,1,1],[1,1,-1],[1,1,1],[-1,1,1],[1,1,1],[1,1,1],[1,-1,-1],[1,1,1],[1,1,1])
weight = []
bias = []
output = []
result = []

#the equation for this network is n = Wp + b and p = W , This is the feedforward layer
for ele in inputs:
    weight.append(ele)
    bias.append(3)
    output = np.dot(inputs,[-1,-1,-1])
output = np.add(output,bias)

# Then we change the weight to correspond to [1,-0.5,....,1,any number smaller than 1]
for w in range(len(weight) - 1):
    weight[w] = 1
    weight[w + 1] = -0.5

#this is the recurrent layer where the network keeps multiplying the new output with the weights 
#until it converges
while np.array_equal(result,output):
    output = np.dot(weight,output)
    




print output
