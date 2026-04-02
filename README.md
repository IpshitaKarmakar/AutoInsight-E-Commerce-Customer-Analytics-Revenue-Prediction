# 🚀 AutoInsight: E-Commerce Customer Analytics & Revenue Prediction

## 📌 Project Overview

This project demonstrates practical skills in:

* Data cleaning and preprocessing
* Exploratory Data Analysis (EDA)
* Business insight generation
* Machine learning modeling

---

## 🎯 Objective

The main goal of this project is to:

* Understand customer purchasing behavior
* Identify revenue-driving factors
* Detect high-value customers
* Build a predictive model for customer segmentation

---

## 📊 Dataset

* Source: Online Retail Dataset (Kaggle)
* Size: ~1 Million records
* Features include:

  * Invoice details
  * Product information
  * Customer ID
  * Country
  * Transaction values

---

## 🛠️ Project Workflow (Step-by-Step)

### 🔹 1. Data Loading

* Loaded raw CSV dataset using Pandas
* Handled encoding issues (`ISO-8859-1`)
* Verified dataset structure and dimensions

---

### 🔹 2. Data Preprocessing

Performed real-world data cleaning:

* Removed missing `CustomerID` values
* Filtered out invalid transactions (negative quantity & price)
* Removed duplicate records
* Standardized column names
* Converted `InvoiceDate` to datetime format

### ➕ Feature Engineering:

* Created `TotalPrice = Quantity × UnitPrice`

---

### 🔹 3. Exploratory Data Analysis (EDA)

Generated meaningful visualizations to understand business patterns:

#### 📈 Monthly Revenue Trend

* Identified seasonal spikes in revenue
* Observed peak sales during holiday periods

#### 🌍 Country-wise Revenue Analysis

* Found that UK dominates overall sales
* Compared other countries by excluding UK for better insights

#### 👥 Customer Purchase Behavior

* Analyzed transaction frequency distribution
* Observed right-skewed behavior (few high-frequency buyers)

#### 🔥 Correlation Analysis

* Strong correlation between Quantity and Revenue
* Weak correlation with Unit Price

#### 🛍️ Top Products Analysis

* Identified most frequently sold products

---

## 📊 Key Insights

* Top 20% customers contribute majority of revenue (Pareto Principle)
* Business is highly concentrated in the UK market
* Sales show strong seasonal trends (holiday-driven demand)
* Customer purchasing behavior is highly skewed
* Revenue is primarily driven by quantity rather than price

---

## 🤖 Machine Learning Model

### 🔹 Objective:

Predict whether a customer is a **high-value customer**

### 🔹 Approach:

* Aggregated customer-level data
* Created target variable based on top 20% revenue

### 🔹 Model Used:

* Random Forest Classifier

### 🔹 Result:

* Achieved ~94% accuracy
* Avoided data leakage by selecting meaningful features

---

## 📁 Project Structure

```
AutoInsight/
 ├── app.py
 ├── utils/
 │    ├── preprocessing.py
 │    ├── analysis.py
 │    ├── modeling.py
 ├── data/
 ├── outputs/
 ├── README.md
```

---

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/your-username/AutoInsight.git
cd AutoInsight
```

### 2. Install dependencies

```bash
pip install pandas matplotlib seaborn scikit-learn
```

### 3. Run the project

```bash
python app.py
```

### 4. Provide dataset path

```
data/online_retail.csv
```

---

## 📌 Output

The project generates:

* Cleaned dataset
* Business insights in terminal
* Visualizations saved in `outputs/`
* Trained machine learning model

---

## 🌍 Open Source Contribution Scope

This project is designed to be **open-source friendly**. Contributions are welcome in:

* Improving visualizations
* Adding new ML models
* Enhancing preprocessing logic
* Building dashboards (Streamlit/Power BI)
* Adding support for large-scale datasets

---

## 🚀 Future Improvements

* Interactive dashboard using Streamlit
* Advanced customer segmentation (RFM Analysis)
* Feature importance visualization
* Real-time data processing support

---

## 💡 Skills Demonstrated

* Data Cleaning & Preprocessing
* Exploratory Data Analysis
* Data Visualization
* Machine Learning
* Problem Solving & Debugging
* Real-world Business Understanding

---

## 📌 Sample Execution Output

Below is a sample run of the project using the Online Retail dataset:

```bash
python app.py
```

```text
Enter the CSV path = data/online_retail.csv

Dataset loaded successfully with shape: (1067371, 8)

Starting preprocessing..
Columns after cleaning: Index(['Invoice', 'StockCode', 'Description', 'Quantity', 'InvoiceDate',
       'Price', 'Customer ID', 'Country'],
      dtype='object')

Data cleaned. Remaining records: 1007914

Analyzing sales and business patterns
Top 10 countries revenue saved
Monthly revenue trend saved
Top products visualization saved
Correlation heatmap saved

Key Insights:
Top 20% customers count: 1176
Revenue contribution by top customers: 13421773.02

Training customer value prediction model...
Model accuracy: 0.94
Training samples: 4702, Testing samples: 1176
```

### 🔍 Interpretation

* Successfully processed **1M+ records**
* Cleaned dataset reduced to ~1M valid transactions
* Identified **top 20% customers contributing major revenue**
* Generated multiple business insights and visualizations
* Achieved **94% accuracy** in predicting high-value customers

This demonstrates the robustness of the pipeline and its applicability to real-world datasets.


## 👩‍💻 Author

**Ipshita Karmakar**
B.Tech CSE | Data Science & AI Enthusiast

