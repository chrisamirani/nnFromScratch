# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 20:30:07 2017

@author: Chris Amirani
"""
# A simple demo of single-neuron perceptron as explined in the book
# feel free to experiment with bigger datasets
import numpy as np

input = [[[0,0],1],[[0,1],0],[[1,0],0],[[1,1],1]]

weight = [2,2]
bias = - np.dot(weight,[1.5,0])
output=[]
def hardlim(weight,input,bias):
    
    for i in range(len(input)):
        a = np.dot(weight,input[i][0]) + bias
        if a >= 0:
            output.append(1)
        else:
            output.append(0)
    print output

hardlim(weight,input,bias);