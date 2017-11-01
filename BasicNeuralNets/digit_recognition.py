#!/usr/bin/env python

import numpy as np
import scipy

class Network:
    """
    base class to create a neural network without tensorflow,
    or any other library
    """
    def __init__(self, sizes: []) -> None:
        """
        construct a neural network with given number of neurons.

        Args:
            sizes: list of number of neurons in each layer
                   i.e. if we have three layers with each having 
                   neurons 3, 5, 4 respectively than input will be
                   sizes = [3, 5, 4]
        """

        # We are not taking no of layers as input.
        self.no_of_layers = len(sizes)

        # Except first layer, each one will be having a bias.
        # Store all bias together in a single matrix.
        # First layer is input hence does not have a bias
        self.bases = [np.random.randn(no_of_neurons, 1)
                    for no_of_neurons in sizes[1:]]

        # Store all the weights. Understanding order of weights is
        # a bit tricky. Weights are from one layer to another hence 
        # they will be of form [neuron_in_layer_1, neuron_in_layer_2]
        # We are taking reverse so we don't need to take a transpose
        # while calculating y = w.x + b
        #self.weights = [np.random.randn(y, x) for x, y in 
