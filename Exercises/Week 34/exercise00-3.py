def accuracy(tp, fp, fn, tn):
    """Arg 1 takes the number of true positives.
    Arg 2 takes the number of false positives.
    Arg 3 takes the number of false negatives.
    Arg 4 takes the number of true negatives.
    The method returns the accuracy of the model."""
    accuracy = (tp + tn)/(tp + tn + fp + fn)
    return accuracy

#Predicting accuracy for a machine learning model that has been trained to predict fire. 
#I would argue that this model is not good, because it results in significantly more false negatives than false positives.
#In this case you would like to have a model that rather gives too many false positives, than false negatives (i.e. a model that is "overly-cautious").

accuracy = accuracy(2, 2, 11, 985)
print(accuracy)