"""
Module for generating and working with various probability distributions.
"""

import numpy as np
import matplotlib.pyplot as plt

def generate_uniform_samples(low=0.0, high=1.0, size=1000):
    """
    Generate random samples from a uniform distribution.

    Parameters:
    low (float): Lower bound of the distribution (default: 0.0)
    high (float): Upper bound of the distribution (default: 1.0)
    size (int): Number of samples to generate (default: 1000)

    Returns:
    numpy.ndarray: Array of uniformly distributed random samples
    """
    return np.random.uniform(low=low, high=high, size=size)

def plot_distribution(samples, bins=30, title="Uniform Distribution"):
    """
    Plot a histogram of the generated samples.

    Parameters:
    samples (array-like): Array of samples to plot
    bins (int): Number of bins for the histogram
    title (str): Title for the plot
    """
    plt.figure(figsize=(10, 6))
    plt.hist(samples, bins=bins, alpha=0.7, edgecolor='black', density=True)
    plt.title(title)
    plt.xlabel('Value')
    plt.ylabel('Density')
    plt.grid(alpha=0.3)
    plt.show()
