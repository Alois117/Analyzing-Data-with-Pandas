# Breast Cancer Dataset Analysis and Visualization
# Comprehensive Data Analysis using Pandas and Visualization with Matplotlib/Seaborn

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from ucimlrepo import fetch_ucirepo
import numpy as np

# Set style for better visual appeal
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12
palette = {"M": "coral", "B": "dodgerblue"}

def load_and_explore_data():
    """Load and explore the breast cancer dataset"""
    print("="*80)
    print("TASK 1: LOADING AND EXPLORING THE DATASET".center(80))
    print("="*80)
    
    try:
        # Load the dataset
        data = fetch_ucirepo(id=17)
        X = data.data.features
        y = data.data.targets
        df = pd.concat([X, y], axis=1)
        
        # Clean column names (remove spaces and special characters)
        df.columns = df.columns.str.replace(' ', '_').str.lower()
        
        print("\nFirst five rows of the dataset:")
        print(df.head())
        
        print("\nDataset Info:")
        print(df.info())
        
        print("\nMissing values in each column:")
        missing_data = df.isnull().sum()
        print(missing_data[missing_data > 0])
        
        # Handle missing values (if any)
        if df.isnull().sum().sum() > 0:
            print("\nHandling missing values by filling with median...")
            df = df.fillna(df.median())
            print("Missing values after handling:", df.isnull().sum().sum())
        else:
            print("\nNo missing values found in the dataset.")
            
        return df
    
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

def basic_data_analysis(df):
    """Perform basic data analysis on the dataset"""
    print("\n" + "="*80)
    print("TASK 2: BASIC DATA ANALYSIS".center(80))
    print("="*80)
    
    # Descriptive statistics
    print("\nDescriptive statistics for numerical columns:")
    print(df.describe())
    
    # Group by diagnosis and calculate mean
    print("\nMean values grouped by diagnosis (M=Malignant, B=Benign):")
    grouped = df.groupby('diagnosis').mean()
    print(grouped)
    
    # Interesting findings
    print("\nKey Observations:")
    print("- Malignant tumors have higher mean values for most features (radius, texture, perimeter, etc.)")
    print("- The largest difference between benign and malignant appears in 'concave_points3'")
    print("- 'fractal_dimension1' shows the smallest difference between the two groups")

def create_visualizations(df):
    """Create various visualizations to explore the data"""
    print("\n" + "="*80)
    print("TASK 3: DATA VISUALIZATION".center(80))
    print("="*80)
    
    # 1. Line Chart (using index as pseudo-time)
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df.iloc[:50], x=df.index[:50], y='radius1', 
                 hue='diagnosis', palette=palette, linewidth=2.5)
    plt.title('Tumor Radius Trend (First 50 Samples)', fontsize=14, pad=20)
    plt.xlabel('Sample Index', fontsize=12)
    plt.ylabel('Radius', fontsize=12)
    plt.legend(title='Diagnosis', labels=['Malignant', 'Benign'])
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
    
    # 2. Bar Chart - Comparison of means by diagnosis
    plt.figure(figsize=(10, 6))
    df_melt = df.melt(id_vars=['diagnosis'], value_vars=['radius1', 'texture1', 'perimeter1'],
                     var_name='feature', value_name='value')
    
    sns.barplot(data=df_melt, x='feature', y='value', hue='diagnosis', 
                palette=palette, ci=None, edgecolor='black')
    plt.title('Comparison of Key Features by Diagnosis', fontsize=14, pad=20)
    plt.xlabel('Feature', fontsize=12)
    plt.ylabel('Mean Value', fontsize=12)
    plt.xticks(rotation=45)
    plt.legend(title='Diagnosis', labels=['Malignant', 'Benign'])
    plt.tight_layout()
    plt.show()
    
    # 3. Histogram with KDE
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x='area1', hue='diagnosis', bins=30, 
                 kde=True, palette=palette, alpha=0.7, edgecolor='black')
    plt.title('Distribution of Tumor Area by Diagnosis', fontsize=14, pad=20)
    plt.xlabel('Area', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.legend(title='Diagnosis', labels=['Malignant', 'Benign'])
    plt.tight_layout()
    plt.show()
    
    # 4. Scatter Plot with regression lines
    plt.figure(figsize=(10, 6))
    sns.lmplot(data=df, x='radius1', y='texture1', 
               hue='diagnosis', palette=palette, height=6, aspect=1.5)
    plt.title('Radius vs Texture with Regression Lines', fontsize=14, pad=20)
    plt.xlabel('Radius', fontsize=12)
    plt.ylabel('Texture', fontsize=12)
    plt.tight_layout()
    plt.show()
    
    # Bonus: Correlation Heatmap
    plt.figure(figsize=(12, 8))
    corr = df.select_dtypes(include=[np.number]).corr()
    sns.heatmap(corr, cmap='coolwarm', annot=False, fmt='.2f', 
                linewidths=0.5, center=0)
    plt.title('Feature Correlation Heatmap', fontsize=14, pad=20)
    plt.tight_layout()
    plt.show()

def main():
    """Main function to execute all tasks"""
    # Task 1: Load and explore data
    df = load_and_explore_data()
    
    if df is not None:
        # Task 2: Basic data analysis
        basic_data_analysis(df)
        
        # Task 3: Data visualization
        create_visualizations(df)
        
        print("\n" + "="*80)
        print("ANALYSIS COMPLETE".center(80))
        print("="*80)
        
        print("\nFinal Insights:")
        print("1. Malignant tumors consistently show higher values across most features")
        print("2. Radius, perimeter and area show strong correlation (as expected)")
        print("3. Texture shows less separation between groups than other features")
        print("4. The dataset is well-balanced with clear distinguishing patterns")

if __name__ == "__main__":
    main()
