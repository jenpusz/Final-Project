# Final-Project

## Goal 
Use machine learning to create a model to predict the likelihood of one's chances for survival upon the RMS Titanic

## Data Preperation
Data was collected from Tensorflow, an online database and cleaned in Python notebooks. We dropped columns that were irrelevant in determining one's survival such as Port of Leave. We then came across the issue of question marks in the data that we converted to null values to later be dropped since the model can not take null values. We then used pandas.get_dummies() method for our <b>gender</b>column in order to change categorical data into dummy or indicator variables, where 0 = "Female" and 1 = "Male".



## Model Building

For this survival predictor, SVM and Logistic Regression Models were used, as these models would be able to classify the binary outcome "Survived" or "Not Survived". Because these models require an array, the data was reshaped before being fed into the model.



The model was compiled and then trained on each of the
## Evaluating and Predicting

## Conclusion
