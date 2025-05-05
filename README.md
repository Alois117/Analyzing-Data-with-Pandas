📊 Breast Cancer Dataset Analysis
📌 Overview
This project performs a comprehensive analysis of the Breast Cancer Wisconsin (Diagnostic) Dataset from the UCI Machine Learning Repository. The objective is to explore, analyze, and visualize the data to understand the distinctions between benign and malignant breast tumors.

🔍 Features
Data Loading & Cleaning
Loads the dataset using ucimlrepo and handles any missing values.

Exploratory Analysis
Displays descriptive statistics and compares feature values grouped by diagnosis.

Data Visualization
Generates multiple informative plots:

Line chart showing tumor radius trends (first 50 samples)

Bar chart comparing average feature values by diagnosis

Histogram showing area distribution

Scatter plot with color-coded diagnoses

Correlation heatmap for numerical features

🧰 Requirements
Python: 3.6+

Packages:

pip install pandas numpy matplotlib seaborn ucimlrepo
🚀 Usage
Clone or download the repository.

Run the analysis script:

python Breast_cancer.py
The script will:

Load and explore the dataset

Output statistical summaries to the console

Generate and display visualizations

📈 Key Findings
Malignant tumors exhibit significantly higher values for most measured features.

The largest difference between tumor types appears in concave point measurements.

Features like radius, perimeter, and area are strongly correlated.

Texture features show less pronounced differences between tumor types.

🖼️ Output
Console Output: Descriptive and grouped statistics.

Visualizations:

Line chart: Tumor radius (first 30 samples)

Bar chart: Feature comparisons (e.g., texture mean)

Histogram: Area mean distribution

Scatter plot: Radius vs. texture

Correlation heatmap of features

📜 License
This project is open-source and available under the MIT License.

🙏 Acknowledgments
Dataset provided by the UCI Machine Learning Repository.
https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic)
