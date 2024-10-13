import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import io
import base64
from flask import Flask, request, render_template, url_for

plt.switch_backend('Agg')
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

app=application

## Route for a home page


@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predict',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('predict.html')
    else:
        data=CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score'))

        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)
        print("after Prediction")
        return render_template('predict.html',results=results[0])
    
@app.route('/visualization')
def visualization():
    # Load the dataset
    df = pd.read_csv('notebook/data/stud.csv')

    # Create visualizations
    # 1. Average Math Scores by Gender
    plt.figure(figsize=(8, 5))
    sns.barplot(x='gender', y='math_score', data=df, hue='gender', palette='coolwarm', legend=False)
    plt.title('Average Math Scores by Gender')
    plt.tight_layout()
    img1 = io.BytesIO()
    plt.savefig(img1, format='png')
    img1.seek(0)
    plot_url1 = base64.b64encode(img1.getvalue()).decode()
    plt.close()

    # 2. Average Writing Scores by Race/Ethnicity
    plt.figure(figsize=(8, 5))
    sns.barplot(x='race_ethnicity', y='writing_score', data=df, hue='race_ethnicity', palette='viridis', legend=False)
    plt.title('Average Writing Scores by Race/Ethnicity')
    plt.xticks(rotation=45)
    plt.tight_layout()
    img2 = io.BytesIO()
    plt.savefig(img2, format='png')
    img2.seek(0)
    plot_url2 = base64.b64encode(img2.getvalue()).decode()
    plt.close()

    # 3. Reading Score vs Writing Score
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x='reading_score', y='writing_score', data=df, hue='gender', palette='deep')
    plt.title('Reading Score vs Writing Score')
    plt.tight_layout()
    img3 = io.BytesIO()
    plt.savefig(img3, format='png')
    img3.seek(0)
    plot_url3 = base64.b64encode(img3.getvalue()).decode()
    plt.close()

    # 4. Distribution of Math Scores
    plt.figure(figsize=(8, 5))
    sns.histplot(df['math_score'], bins=20, kde=True)
    plt.title('Distribution of Math Scores')
    plt.tight_layout()
    img4 = io.BytesIO()
    plt.savefig(img4, format='png')
    img4.seek(0)
    plot_url4 = base64.b64encode(img4.getvalue()).decode()
    plt.close()

    # 5. Boxplot of Math Scores by Gender
    plt.figure(figsize=(8, 5))
    sns.boxplot(x='gender', y='math_score', data=df, palette='Set2')
    plt.title('Boxplot of Math Scores by Gender')
    plt.tight_layout()
    img5 = io.BytesIO()
    plt.savefig(img5, format='png')
    img5.seek(0)
    plot_url5 = base64.b64encode(img5.getvalue()).decode()
    plt.close()

    # 6. Correlation Heatmap
    plt.figure(figsize=(8, 5))
    correlation_matrix = df[['math_score', 'reading_score', 'writing_score']].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap of Scores')
    plt.tight_layout()
    img6 = io.BytesIO()
    plt.savefig(img6, format='png')
    img6.seek(0)
    plot_url6 = base64.b64encode(img6.getvalue()).decode()
    plt.close()

    # Render the template and pass the URLs of the plots
    return render_template('visualization.html', plot_url1=plot_url1, plot_url2=plot_url2, plot_url3=plot_url3,
                           plot_url4=plot_url4, plot_url5=plot_url5, plot_url6=plot_url6)


data=pd.read_csv('notebook/data/stud.csv')

@app.route('/dataset')
def dataset():
    # Convert the DataFrame to HTML table
    df = pd.read_csv('notebook/data/stud.csv')
    data = df.to_dict(orient='records')
    return render_template('dataset.html', data=data)

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)        

