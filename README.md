# 🚲 Bike Rental Demand Forecasting using Machine Learning and Clustering Techniques

## 📌 Project Overview

This project addresses the critical challenge of predicting demand for bike rentals in urban environments by analyzing daily, seasonal, and weather-related factors. By leveraging a comprehensive analytical framework and applying both classification and predictive modelling techniques, this study aims to enhance operational efficiency and support sustainable urban mobility planning.

## 🎯 Objectives

- Identify key environmental and temporal factors affecting bike rental demand.
- Classify expected bike rental demand into operational categories (low, medium, high).
- Forecast future rental demand using historical weather and usage data.
- Evaluate and compare the performance of various predictive models.

## 🗂 Dataset Description

- **Source**: [Kaggle - Bike Sharing Dataset](https://www.kaggle.com/datasets)
- **Size**: 10,886 observations with 17 features
- **Target Variable**: `rentals`
- **Features**: Include `season`, `hour`, `temperature`, `humidity`, `windspeed`, `holiday`, `workingday`, `weather`, and user type (`casual`, `registered`)

## 🔍 Exploratory Data Analysis (EDA)

- **Univariate Analysis**: Distribution plots for key features (temperature, humidity, windspeed)
- **Bivariate Analysis**: Boxplots for bike rentals vs. time of day, season, and month
- **Proximity Analysis**: Correlation heatmaps to understand inter-feature relationships

## 🧹 Data Preprocessing

- Handled missing values 
- Performed descriptive statistical analysis
- Standardized and normalized continuous variables
- Encoded categorical features appropriately
- Removed redundant features (e.g., high collinearity between `temp` and `atemp`)

## 🧪 Machine Learning Models Applied

### Clustering Techniques
- **K-Means Clustering**
- **Hierarchical Clustering**

### Classification Algorithms
- **Support Vector Machine (SVM)**
- **Random Forest Classifier**

### Regression Models
- **Ridge Regression**
- **Artificial Neural Networks (Multilayer Perceptrons)**

## 📈 Model Evaluation Metrics

- **Classification Accuracy**
- **Mean Absolute Error (MAE)**
- **Mean Squared Error (MSE)**
- **Root Mean Square Error (RMSE)**

### Key Insights:
- **Random Forest** performed slightly better in high-demand prediction scenarios.
- **Multilayer Perceptrons (MLP)** were effective in modeling non-linear demand patterns.
- Environmental variables such as **temperature, humidity, and windspeed** significantly influenced demand.

## 📊 Tools & Libraries

- Python (Pandas, NumPy, Matplotlib, Seaborn)
- Scikit-learn
- TensorFlow / Keras (for ANN)
- Jupyter Notebook
