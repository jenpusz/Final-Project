# Final-Project

## Goal 
Use machine learning to create a model to predict the likelihood of one's chances for survival upon the RMS Titanic

## Data Preperation
Data was collected from Tensorflow, an online database and cleaned in Python notebooks. We dropped columns that were irrelevant in determining one's survival such as Port of Embarktion. We then came across the issue of question marks in the data that we converted to null values. Because our dataset was already small, we did not want to drop the null values, but replace them with the mean for <u>Age</u>, and mode for <u>Embarked</u> and <u>Fare</u>.  We then used pandas.get_dummies() method for our <b>gender</b> column in order to change categorical data into dummy or indicator variables, where 0 = "Female" and 1 = "Male".

### Data Dictionary
survival 0 = No, 1 = Yes
pclass Ticket class 1 = 1st, 2 = 2nd, 3 = 3rd
pclass: A proxy for socio-economic status (SES)
1st = Upper
2nd = Middle
3rd = Lower
sex Sex
Age Age in years
sibsp # of siblings / spouses aboard the Titanic -sibsp: The dataset defines family relations in this way...

  - Sibling = brother, sister, stepbrother, stepsister
  - Spouse = husband, wife (mistresses and fiancés were ignored)
parch # of parents / children aboard the Titanic

parch: The dataset defines family relations in this way...
Parent = mother, father
Child = daughter, son, stepdaughter, stepson
Some children travelled only with a nanny, therefore parch=0 for them.
ticket Ticket number

fare Passenger fare
cabin Cabin number
embarked Port of Embarkation C = Cherbourg, Q = Queenstown, S = Southampton

## Model Building

For this survival predictor, SVM and Logistic Regression Models were used, as these models would be able to classify the binary outcome "Survived" or "Not Survived". Because these models require an array, the data was reshaped before being fed into the model.



The model was compiled and then trained on each of the
## Evaluating and Predicting

## Conclusion
