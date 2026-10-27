import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load public dataset (Titanic from seaborn)
df = sns.load_dataset('titanic')

# Basic info
print('Shape:', df.shape)
print(df.head())
print(df.info())
print(df.describe())

# Missing values
print('\nMissing values:')
print(df.isnull().sum())

# Univariate analysis
plt.figure(figsize=(6,4))
sns.countplot(data=df, x='survived')
plt.title('Survival Count')
plt.savefig('survival_count.png')
plt.close()

plt.figure(figsize=(6,4))
sns.countplot(data=df, x='sex')
plt.title('Gender Distribution')
plt.savefig('gender_distribution.png')
plt.close()

plt.figure(figsize=(6,4))
sns.histplot(data=df, x='age', bins=20, kde=True)
plt.title('Age Distribution')
plt.savefig('age_distribution.png')
plt.close()

# Bivariate analysis
plt.figure(figsize=(6,4))
sns.countplot(data=df, x='sex', hue='survived')
plt.title('Survival by Gender')
plt.savefig('survival_by_gender.png')
plt.close()

plt.figure(figsize=(6,4))
sns.boxplot(data=df, x='pclass', y='age')
plt.title('Age by Passenger Class')
plt.savefig('age_by_class.png')
plt.close()

# Correlation
plt.figure(figsize=(8,6))
corr = df.select_dtypes(include=['number']).corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.savefig('correlation_heatmap.png')
plt.close()

print('Analysis complete. Charts saved.')
