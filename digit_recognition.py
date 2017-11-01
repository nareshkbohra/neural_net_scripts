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
    	no_of_layers = len(sizes)

        # Except first layer, each one will be having a bias.
        # Store all bias together in a single matrix.
        # First layer is input hence does not have a bias
    	bases = [np.random.randn(no_of_neurons, 1)
    	            for no_of_neurons in sizes[1:]]

    	# Store all the weights. Understanding order of weights is
    	# a bit tricky.
    	#weights = [np.randon.randn(

def main():
    """
    Driver function to test functionality.
    """

    net = Network([1, 2, 3])

if __name__ == "__main__":
    main()
