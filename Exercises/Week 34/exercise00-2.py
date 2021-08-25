def compute_accuracy(correct, total):
    """Arg 1 takes the number of correct predictions and arg 2 takes the total number of predictions.
    The model returns the accuracy of the model as a number between 0 (0%) and 1 (100%)."""
    return correct/total

#Count the accuracy of a model for weather prediction
print(compute_accuracy(300, 365))