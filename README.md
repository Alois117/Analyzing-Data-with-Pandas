🧠 Breast Cancer Wisconsin Dataset Analysis
📊 Overview
This project performs a comprehensive analysis of the Breast Cancer Wisconsin (Diagnostic) dataset fetched directly from the UCI Machine Learning Repository using the ucimlrepo Python package. The analysis includes data exploration, statistical analysis, and visualization to help understand patterns between benign and malignant tumors.

✅ Features
Data Loading & Cleaning: Dataset is loaded via ucimlrepo and checked for missing values.

Exploratory Data Analysis: Descriptive statistics and group-wise comparisons by diagnosis.

Data Visualization: Includes the following plots:

Line Chart: Tumor radius trends across samples.

Bar Chart: Comparison of key features by tumor type.

Histogram: Distribution of tumor areas.

Scatter Plot: Relationship between radius and texture with diagnosis hue.

Correlation Heatmap: Relationship among all numerical features.

📦 Requirements
Python 3.6+

Required packages:

pip install pandas numpy matplotlib seaborn ucimlrepo
🛠️ Installation & Usage
Clone the repository:

git clone https://github.com/Alois117/Analyzing-Data-with-Pandas.git
Run the script:

python breast_cancer_analysis.py
The script will:

Load and explore the dataset

Print summary statistics

Generate 5 interactive visualizations sequentially

📈 Visualization Details
Line Chart: Displays how tumor radius varies across the first 50 samples

Bar Chart: Mean values of radius, texture, and area for benign vs malignant cases

Histogram: Frequency distribution of tumor areas with KDE overlay

Scatter Plot: Radius vs. texture with regression lines by diagnosis

Heatmap: Color-coded matrix showing feature correlations

🧪 Key Findings
Malignant tumors consistently have higher values in most metrics

Largest differences observed in concave points

Radius, perimeter, and area features are strongly correlated

Texture values are less distinct across tumor types

📚 Acknowledgments
Dataset sourced from the UCI Machine Learning Repository

Accessed via the ucimlrepo Python package

📝 License
This project is open source and available under the MIT License.
