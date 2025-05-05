**# Breast Cancer Wisconsin Dataset Analysis**

**## Complete Data Analysis with Visualizations**

This project performs a comprehensive analysis of the Breast Cancer Wisconsin (Diagnostic) Dataset, including five different visualizations to explore the data.

**## Features**

- **Complete Data Analysis Pipeline**:
  - Data loading and cleaning
  - Statistical analysis
  - Visualization generation

- **Five Interactive Visualizations**:
  1. **Line Chart**: Shows tumor radius trends across samples
  2. **Bar Chart**: Compares key features between benign and malignant tumors
  3. **Histogram**: Displays distribution of tumor areas by diagnosis
  4. **Scatter Plot**: With regression lines showing radius vs texture relationship
  5. **Correlation Heatmap**: Visualizes relationships between all numerical features

**## Requirements**

- Python 3.6+
- Required packages:
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - ucimlrepo

**Install with:**
pip install pandas numpy matplotlib seaborn ucimlrepo

Usage
Run the analysis script:
python Breast_cancer.py
The script will:

Load and explore the dataset

Perform statistical analysis

Generate all five visualizations in sequence

Visualization Details
Line Chart: Shows how tumor radius varies across the first 50 samples

Bar Chart: Compares mean values of radius, texture, and area between tumor types

Histogram: Shows frequency distribution of tumor areas with KDE overlay

Scatter Plot: With separate regression lines for each diagnosis type

Heatmap: Color-coded correlation matrix of all numerical features

Key Findings
Malignant tumors consistently show higher values across most features

The largest differences appear in concave points measurements

Radius, perimeter and area features are strongly correlated

Texture features show less separation between tumor types

License
This project is open source and available under the MIT License

This complete version will generate all five visualizations in sequence. Each visualization will appear in its own window - you'll need to close each one to see the next. The visualizations use the correct column names from your dataset (radius1, texture1, etc.) and provide clear insights into the differences between benign and malignant tumors.

Acknowledgments
Data sourced from the UCI Machine Learning Repository:
https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic)
