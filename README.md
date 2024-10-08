# Student Score Predictor - Aradhya Shukla 🧑🏻‍🎓🌟

### Introduction About the Data :

#### Dataset: Students Performance in Exams - https://www.kaggle.com/code/aryanml007/students-performance-analysis/input

## Description

This dataset contains information about student performance on exams, including:

- `gender`: Gender of the student (male/female)
- `ethnicity`: Ethnicity of the student
- `parental_level_of_education`: Highest education level of the student's parents
- `lunch`: Type of lunch the student has (standard or free/reduced)
- `test_preparation_course`: Whether the student completed a test preparation course (completed or none)
- `math_score`: Score obtained in the math exam
- `reading_score`: Score obtained in the reading exam
- `writing_score`: Score obtained in the writing exam

**Size:** The dataset consists of approximately 1000 rows (students) and 8 columns (features).


## Approach for the project 

1. Data Ingestion : 
    * In Data Ingestion phase the data is first read as csv. 
    * Then the data is split into training and testing and saved as csv file.

2. Data Transformation : 
    * In this phase a ColumnTransformer Pipeline is created.
    * for Numeric Variables first SimpleImputer is applied with strategy median , then Standard Scaling is performed on numeric data.
    * for Categorical Variables SimpleImputer is applied with most frequent strategy, then ordinal encoding performed , after this data is scaled with Standard Scaler.
    * This preprocessor is saved as pickle file.

3. Model Training : 
    * In this phase base model is tested . The best model found was catboost regressor.
    * After this hyperparameter tuning is performed on catboost and knn model.
    * A final VotingRegressor is created which will combine prediction of catboost, xgboost and knn models.
    * This model is saved as pickle file.

4. Prediction Pipeline : 
    * This pipeline converts given data into dataframe and has various functions to load pickle files and predict the final results in python.

5. Flask App creation : 
    * Flask app is created with User Interface to predict the gemst

## Possible Uses

- Analyze factors influencing student performance
- Identify areas for improvement in educational programs
- Predict student performance based on various factors
- Gender Performance: Compare performance between male and female students.
- Ethnicity Impact: Assess how ethnicity affects academic results.
- Parental Education: Explore the influence of parents' education levels on student scores.
- Lunch Type: Determine if lunch standard impacts student performance.
- Test Preparation:</strong> Evaluate the effect of test prep courses on exam scores.

## Target Variable

- `math_score`: Score obtained in the math exam

# AZURE Deployment Link :

(https://scorepredictor.aradhya.site/)

# Screenshot of UI
![Screenshot (247)](https://github.com/user-attachments/assets/b5d434cc-bb06-4585-9bd2-f522ca371c7d)


one prices inside a Web Application.

