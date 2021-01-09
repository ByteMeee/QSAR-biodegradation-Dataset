# QSAR-biodegradation-Dataset

This project is all about how to analyse the QSAR biodegradation Dataset which is open source and how to create and train a machine learning model to predict(classifie) if an entry in the Dataset ready biodegradable (RB) and not ready biodegradable (NRB).

Link to the dataset: https://archive.ics.uci.edu/ml/datasets/QSAR+biodegradation#

The first step of was to visualize the dataset and see if he was linearly separable using a correlation matrix and a PCA.

In The second part we trained and tested multiple models using a train set containing 70% of the original dataset and a test set using the rest of the dataset.

The result where that the decision tree and logestic regression were better then the other models.

For the conclusion: we used the decision tree model to create an API with Flask but this model can be improved by using dummy variables for the columns that have cathegorical values and it can be improved too by using a sub-dataset with a classes that are more equally distributed then the original dataset. 

P.s: its better to try the API in google colab using this link : https://colab.research.google.com/drive/1U7giOtvbvW7Xs2NmtTrPPlAfVlA2cXnf?usp=sharing
