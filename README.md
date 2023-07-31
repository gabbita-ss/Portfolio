# Who am I?

Hey there! I am Chandrahas Gabbita, a recent graduate from Stony Brook University. I am a double major in Physics and Mathematics and am interested in the      field of Data Analysis and Data Science. Over the last year, I have been learning data science through a combination of coursework, certifications, and          projects. It has been a fascinating journey and if you'd like to learn more about it, take a look at my resume below and keep scrolling!

[Take a look at my resume](https://github.com/gabbita-ss/Portfolio/blob/main/CG%20.pdf)

## What can I do?
I can help draw insights and predictions from data starting with exploratory data analysis to model validation, testing, and visualization. My coursework         includes advanced Physics and Math, Statistics, Data Analysis (Regression Modelling), and Machine Learning for Quantitative Finance. I have completed the         Google Advanced Data Analytics certification during which I familiarized myself with many more machine learning methods especailly suited for tabular data.

[My Google Advanced Data Analytics certification](https://github.com/gabbita-ss/Portfolio/blob/main/Certification.pdf)

## I am skilled in the following areas:

**Programming Languages**
- I am an expert in Python
- I am experienced in statistical programming in R
- MATLAB

**Machine Learning**
- Model validation and testing
- Linear and Logistic regression
- Descision trees, Random forests, Gradient boosted trees
- Clustering algorithms such as k-means
- Naive Baye's classification and regression

**Deep Learning** 
- Feed Forward and Convolutional Neural Networks

**My Data Analytics Skills Other Than The Ones Listed Above:**
- Exploratory data analytics and visualization in python


# My Projects 

## Google Advanced Data Analytics Capstone Project

[Look at the project, results, and visualtizations here!](https://nbviewer.org/github/gabbita-ss/Portfolio/blob/main/Google%20Advanced%20Data%20Analytics%20Project.ipynb)

<details>
<summary><b>Click here to view the capstone project description!</b></summary></summary>

As a part of the Google Advanced Data Analytics certification, I have completed a data analysis profject from beginning to end. The project deals with a        hypothetical Salifort Motors, and aims to predict employee retention in the company. The goal of the project is to determine whether an employee will stay in   the company or churn (leave) based on a set of features. The data set contains data collected from employees on a variety of factors such as their satisfaction level, salary, and the number of years they have worked for the company etc. In addition, the data also includes whether the employee stayed in the company or left. This data set was borrowed from Kaggle and can be accessed [here](https://www.kaggle.com/datasets/leviiiest/salifort-motor-hr-dataset?select=HR_capstone_dataset.csv). The data format is as follows:

![Test](https://raw.githubusercontent.com/gabbita-ss/Portfolio/main/docs/assests/images/Google-data-format.jpg)

The project includes the following stages:

**Exploratory Data Analysis**
- The data was examined and the appropriate statistics were determined and outliers were noted
- Different variables were compared to determine the strongest predictors of employee churn
- Key insights were drawn on the predictors of employee churn

**Data Pre-Processing**
- Missing values in the data were removed
- The data was divided into three sections - train, validation, and test data (in a 0.8 - 0.2 - 0.2 split)

**Model Building and Validation**
- The best metric to train the models on was determined to be "recall" becasue of the the unequal representation of classes in the dataset
- Two models were built - a random forest model and a gradient boosted tree model
- Hyperparameters were tuned for both models using cross validation with 5 folds on the train data
- Both models were validated against each other on the validation data to determine champion model
- The champion model (the gradient boosted tree model) was tested on the test data

**Testing and Insights**
- The model performed extremely well on the test data with an accuracy of 98%, precision of 97%, and recall of 93%.
- The most significant factors affecting employee retention were determined

</details>

## Senior Lab Course Experiment (Regression)
[Look at the project code, data analysis, and visualization here!](https://nbviewer.org/github/gabbita-ss/Portfolio/blob/main/Compton%20final.ipynb)

<details> <summary><b>Click here to look at the regression project description!</b></summary>  
This experiment was part of my PHY 445 (Senior Physics Lab) coursework and was on a physics scattering phenomenon called Compton Scattering. The experiment included collecting scattering and background noise data at 10 different angles of the setup. The form of data collected is of the form of "number of scattering events" for each given "energy bin". Therefore, it is frequency data and follows a poisson distribution. The corrected data is the result of subtracting the background noise dataset from the dcattering datasets. The corrected data is expected to contain two peaks and therefore can be fit with two gaussians. One of the 10 cleaned datasets after data preprocessing (described below) and the fit is as follows:

![Compton Scattering data with fit](https://raw.githubusercontent.com/gabbita-ss/Portfolio/main/docs/assests/images/Compton-data-format_1.jpg)

The goal of the project was to track the location of larger peak on the energy bin axis through all 10 angles or datasets with it's associated uncertainty. and plot the energy-bin location of the peak as a function of the angle. A regression model of the expected theoretical curve is fit with the "electron mass" as the free parameter to determine and verify the electron mass with the accepted value in literture (~511 keV). [The detailed overview of the physics, the data analysis, model used, and the results and conclusions can be found here.](https://github.com/gabbita-ss/Portfolio/blob/main/Compton.pdf) 

The dataset consists of a set of 20 datasets of frequency data - 10 scattering datasets and 10 background datasets in total - one scattering and background frequency data for each angle. In order to accomplish this goal the following steps were followed:

**Exploratory Data Analysis**
- Form of data was examined and the poisson model of the data was noted
- Datasets were examined for skewness and outliers
- The appropriate regression model to fit the scattering data was determined to be a sum of two gaussians  

**Data Pre-Processing**
- The background noise datasets were subtracted from each of the scattering datasets giving a total of 10 cleaned datasets
- The data was rescaled appropriately for the following analysis
- Frequency data was corrected for the sensitivity of the equipment as a function of energy bin number
- The two-gaussian regression model was fit to the corrected datasets for each of the 10 angles
- The means and standard deviation of the peaks were noted and plotted against angle

The result of the data preprocessing is the following:

![Energy-Angle relationhsip](https://raw.githubusercontent.com/gabbita-ss/Portfolio/main/docs/assests/images/Energy-Angle_1.jpg)

**Model Building and Validation**
- The appropriate regression curve was fit to the Energy-Angle plot
- The regression parameter (electron mass) was determined using weighted least-squares
- A Chi-squared test was performed to check validity of fit 

![Energy_Angle fit](https://raw.githubusercontent.com/gabbita-ss/Portfolio/main/docs/assests/images/Energy-Angle-fit.jpg)

**Testing and Insights**
- The chi-squared obtained was 0.03 for 9 degrees of freedom and the derived mass of the electron was 511.57 keV with an uncertainty of 77.51 keV which agrees with literature (510.998 keV)

</details>

## Stony Brook Cosmology Group Research

[Click here to view the main coding files for the project!](https://github.com/gabbita-ss/Portfolio/tree/main/BMX)

<details><summary><b>Click here to view the Cosmology project description and results!</b></summary>
I have worked in the Stony Brook Plasma Physics research group to analyze data from a radio telescope called BMX. The telescope observed the sky for signals belonging to a certain frequency range each day. Therefore, the data consisted of hundreds of datasets of image data where the x-axis represented time and the y-axis the frequency. The intensity of a signal at a certain frequency and time can be plotted on a heatmap like in the one below:

![Raw BMX data](https://raw.githubusercontent.com/gabbita-ss/Portfolio/main/docs/assests/images/raw.png)

However, it is clear that the data is noisy and distorted. The noise in the data occurs from the amplification of the signal by the telescope and is random in time. The distortion, known as doppler shift, is much more subtle and can be seen through the slight arching of the dark blue line connecting the two clusters in the image. The goal of the project was to remove this noise and distortion from the image and followed the following steps.

**Exploratory Data Analysis**
- The data was explored and the different types of noise in the data were examined
- Data that was too corrupt was removed

**Data Pre-Processing**
- The noise in the data was removed by fitting a regression line through every column of the dataset to model the expected form of the noise and dividing it out of the dataset
- The doppler shift in the data was corrected using complex image processing techniques

**Results and Insights**

The result of the code written can be seen in the following figure:

![Data transformation](https://raw.githubusercontent.com/gabbita-ss/Portfolio/main/docs/assests/images/BMX%20data%20transformation.jpg)
  
</details>

## Stony Brook Plasma Group Research

<details><summary><b>Click here to look at the plasma research project description!</b></summary>

As part of this project, I was tasked with interpolating low resolution 2-D plasma simulation images to obtain higher resolution images. The aim of the project is to help the team decide on whether interpolation was the right method to improve simulation resolution. The project was mainly image processing and included the following steps:

**Processing**
- Designed and implemented multiple interpolation techniques such as quadratic, cubic splines and radial basis function interpolation to determine the ideal method

</details>






