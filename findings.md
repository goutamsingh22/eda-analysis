# Key Findings - Titanic EDA

## Dataset Overview
- Shape: 891 rows × 15 columns
- Public dataset from Seaborn's built-in datasets
- Target variable: survived (0 = No, 1 = Yes)

## Missing Data
- age: ~177 missing values
- embarked: 2 missing values
- deck: large number of missing values (dropped/ignored in analysis)
- embarked_town: 2 missing values

## Key Insights

### Survival
- Overall survival rate was lower than non-survival (more passengers died)
- Females had significantly higher survival rate than males
- Women and children first pattern is evident

### Demographics
- Majority of passengers were male
- Age distribution is right-skewed with most passengers between 20-40 years
- Third class had younger passengers on average

### Class Impact
- First class passengers had higher survival rates
- Socioeconomic status (passenger class) strongly influenced survival
- Strong correlation between fare and class/survival

## Visualizations Generated
1. survival_count.png - Overall survival distribution
2. gender_distribution.png - Gender breakdown
3. age_distribution.png - Age histogram
4. survival_by_gender.png - Survival rates by gender
5. age_by_class.png - Age distribution across classes
6. correlation_heatmap.png - Feature correlations
