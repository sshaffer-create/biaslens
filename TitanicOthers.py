# ===================== LIBRARIES TO INSTALL =====================
# Run these in terminal before running this file:
# pip install pandas
# pip install numpy
# pip install matplotlib
# pip install seaborn
# pip install scipy
# pip install scikit-learn


# ===================== IMPORT LIBRARIES =====================
import pandas as pd  # pandas is used to load, clean, and analyze tabular data
import numpy as np  # numpy is used for numerical operations and conditional logic
import matplotlib.pyplot as plt  # matplotlib is used for basic plotting
import seaborn as sns  # seaborn is used for improved statistical visualizations
from sklearn.preprocessing import StandardScaler  # StandardScaler is used to standardize numeric variables


# ===================== LOAD TITANIC DATA =====================
titanic = pd.read_csv("titanic.csv")  # Load the Titanic CSV file into a pandas DataFrame named titanic
# titanic = pd.read_excel("titanic.xlsx")  # Use this instead if your Titanic file is in Excel format
#if your file isn't in the same folder where your .py file is, we do the following:
#titanic = pd.read_csv("C:/Users/Shwadhin Sharma/Downloads/titanic.csv")  # Load file from Downloads folder
#if there are multiple worksheet in the excel file, you can import both in the following way:
#titanic_sheet1 = pd.read_excel("titanic.xlsx", sheet_name="Sheet1")  # Load Sheet1 or the sheet name into a dataframe
#titanic_sheet2 = pd.read_excel("titanic.xlsx", sheet_name="Sheet2")  # Load Sheet2 or the sheet name into a dataframe


print(titanic.head(5))  # Show the first 5 rows to confirm the file loaded correctly


# ===================== CHECK AND REMOVE DUPLICATES =====================
duplicate_count = titanic.duplicated().sum()  # Count the number of duplicate rows in the dataset
print("Number of duplicate rows:", duplicate_count)  # Print the number of duplicate rows

titanic_clean = titanic.drop_duplicates()  # Create a cleaned version of the dataset with duplicate rows removed
print("Shape before removing duplicates:", titanic.shape)  # Print the original number of rows and columns
print("Shape after removing duplicates:", titanic_clean.shape)  # Print the new number of rows and columns after duplicates are removed


# ===================== OUTLIER DETECTION USING IQR FOR FARE =====================
q1 = titanic['fare'].quantile(0.25)  # Calculate the first quartile of the fare column
q3 = titanic['fare'].quantile(0.75)  # Calculate the third quartile of the fare column
iqr = q3 - q1  # Compute the interquartile range of the fare column

lower_bound = q1 - 1.5 * iqr  # Calculate the lower bound for outlier detection
upper_bound = q3 + 1.5 * iqr  # Calculate the upper bound for outlier detection

fare_outliers = titanic[(titanic['fare'] < lower_bound) | (titanic['fare'] > upper_bound)]  # Select rows where fare is below or above the outlier limits
print("Number of fare outliers:", fare_outliers.shape[0])  # Print the total number of fare outliers
print(fare_outliers[['fare', 'pclass', 'survived']].head(10))  # Display the first 10 outlier rows with selected columns


# ===================== CROSSTAB WITH COUNTS =====================
survival_gender_table = pd.crosstab(titanic['sex'], titanic['survived'])  # Create a frequency table for sex and survival
print(survival_gender_table)  # Print the crosstab count table


# ===================== CROSSTAB WITH PERCENTAGES =====================
survival_gender_percent = pd.crosstab(titanic['sex'], titanic['survived'], normalize='index') * 100
# Create a row percentage table for sex and survival
print(survival_gender_percent)  # Print the crosstab percentage table


# ===================== PIVOT TABLE ANALYSIS =====================
pivot_table_result = pd.pivot_table(titanic, values='fare', index='pclass', columns='sex', aggfunc='mean')
# Calculate average fare by passenger class and sex
print(pivot_table_result)  # Print the pivot table result


# ===================== FEATURE ENGINEERING: FAMILY SIZE =====================
#Factor plot for Family_Size (Count Feature) and Family Size.  Family_Size denotes the number of people in
# a passenger’s family. It is calculated by summing the SibSp and Parch columns of a respective passenger.
# Also, another column Alone is added to check the chances of survival of a lone passenger against the one with a family.

titanic['family_size'] = titanic['sibsp'] + titanic['parch'] + 1
# Create a new family size column by adding siblings, parents, and the passenger
print(titanic[['sibsp', 'parch', 'family_size']].head(10))
# Show the first 10 rows of the family size calculation

print(titanic.groupby('family_size')['survived'].mean())  # Calculate and print survival rate by family size


# ===================== FEATURE ENGINEERING: IS ALONE =====================
titanic['is_alone'] = np.where(titanic['family_size'] == 1, 1, 0)
# Create a binary variable where 1 means the passenger traveled alone and 0 is not alone
# Create a new column 'is_alone'
# np.where(condition, value_if_true, value_if_false)
# If family_size == 1 → passenger is alone → assign 1. Else → passenger is NOT alone → assign 0

titanic['is_alone'] = np.where(titanic['family_size'] == 1, 1, 0)
print(titanic[['family_size', 'is_alone']].head(10))  # Show the first 10 rows of family size and is alone

print(titanic.groupby('is_alone')['survived'].mean())  # Calculate and print survival rate for alone versus not alone passengers


# ===================== FEATURE ENGINEERING: FARE GROUP =====================
titanic['fare_group'] = pd.cut(titanic['fare'], bins=[0, 10, 30, 100, 600], labels=['Low', 'Medium', 'High', 'Very High'])  # Categorize fare into groups
print(titanic[['fare', 'fare_group']].head(10))  # Show the first 10 rows of fare and fare group

print(titanic.groupby('fare_group')['survived'].mean())  # Calculate and print survival rate by fare group


# ===================== HANDLE MISSING AGE VALUES BEFORE SCALING =====================
titanic['age_filled'] = titanic['age'].fillna(titanic['age'].median())  # Replace missing age values with the median age
print(titanic[['age', 'age_filled']].head(10))  # Show the first 10 rows comparing original age and filled age


# ===================== STANDARDIZE AGE AND FARE =====================
scaler = StandardScaler()  # Create a StandardScaler object
scaled_values = scaler.fit_transform(titanic[['age_filled', 'fare']])  # Standardize the age_filled and fare columns

scaled_df = pd.DataFrame(scaled_values, columns=['age_scaled', 'fare_scaled'])  # Convert the standardized values into a new dataframe
print(scaled_df.head(10))  # Print the first 10 rows of the scaled dataframe


# ===================== ONE HOT ENCODING FOR SEX =====================
sex_dummies = pd.get_dummies(titanic['sex'], prefix='sex', drop_first=True)  # Convert the sex column into dummy variables and drop one category
print(sex_dummies.head(10))  # Print the first 10 rows of the dummy variables

titanic = pd.concat([titanic, sex_dummies], axis=1)  # Add the dummy variable columns back into the main dataframe
print(titanic.head(10))  # Print the first 10 rows to confirm the new columns were added


# ===================== SORT PASSENGERS BY FARE =====================
highest_fare_passengers = titanic.sort_values(by='fare', ascending=False)  # Sort the dataset from highest fare to lowest fare
print(highest_fare_passengers[['name', 'fare', 'pclass', 'survived']].head(10))  # Print the top 10 passengers who paid the highest fare


# ===================== FILTER A SUBGROUP =====================
female_first_class = titanic[(titanic['sex'] == 'female') & (titanic['pclass'] == 1)]  # Filter only female passengers in first class
print(female_first_class[['name', 'age', 'fare', 'survived']].head(10))  # Show the first 10 rows of the filtered subgroup

print("Survival rate of first class females:", female_first_class['survived'].mean())  # Print the survival rate of female first class passengers


# ===================== VISUALIZE FAMILY SIZE VS SURVIVAL =====================
sns.barplot(x='family_size', y='survived', data=titanic)  # Create a bar plot showing survival rate by family size
plt.xlabel('Family Size')  # Label the x-axis
plt.ylabel('Average Survival Rate')  # Label the y-axis
plt.title('Survival Rate by Family Size')  # Add a title to the chart
plt.show()  # Display the chart

#Bar Plot for Fare (Continuous Feature)
#Fare denotes the fare paid by a passenger. As the values in this column are continuous,
# they need to be put in separate bins (as done for Age feature) to get a clear idea. It can be concluded that if a passenger paid a higher fare, the survival rate is more.
# Divide Fare into 4 bins and then use the variable created below into our next line of code
titanic['Fare_Range'] = pd.qcut(titanic['fare'], 4)
# Barplot - Shows approximate values based on the height of bars. We are using variable we created above for this barplot.
sns.barplot(x ='Fare_Range', y ='survived', data = titanic)

# Create a categorical count plot using seaborn
sns.catplot(
    x='embarked',        # X-axis: Port where passenger boarded (C, Q, S)
    hue='survived',      # Split bars by survival (0 = died, 1 = survived)
    kind='count',        # Count number of passengers (frequency)
    col='pclass',        # Create separate plots for each passenger class (1st, 2nd, 3rd)
    data=titanic         # Dataset being used
)

# ===================== SAVE UPDATED FILE =====================
titanic.to_csv("titanic_updated.csv", index=False)  # Save the updated dataframe as a new CSV file without row numbers
print("Updated Titanic file saved successfully.")  # Confirm that the updated file has been saved


################## What if I want to Concatenate (i.e., Stack) two files on top of one another #################
import pandas as pd  # Import pandas to work with dataframes

# LOAD two files first into Python. Both files are in my Python folder already.
df1 = pd.read_csv("titanic_part1.csv")  # Load first part of the dataset
df2 = pd.read_csv("titanic_part2.csv")  # Load second part of the dataset

# CONCAT (ROW-WISE)
apple = pd.concat([df1, df2], axis=0)  # Stack df1 and df2 vertically (add rows)
# axis = 0 means combine data row-wise (stack rows, one below another)
# axis = 1 means combine data column-wise (add columns side by side)

print(apple.shape)  # Show total number of rows and columns after combining
print(apple.head(10))  # Show first 10 rows of the combined dataset

# RESET INDEX so that the first column does say 0,1,2 and and 0, 1, 2 again
appleCorrect = apple.reset_index(drop=True)  # Reset index so it runs from 0 to n without duplication
print(appleCorrect.head(10))  # Show first 10 rows after fixing index

# SAVE COMBINED FILE to Python Project folder
appleCorrect.to_csv("titanic_concat.csv", index=False)  # Save the combined dataset as a new CSV file
print("Concatenated file saved successfully.")  # Confirm that the file was saved

################## What if I want to Merge (i.e., Join) two files using a common column #################
import pandas as pd  # Import pandas to work with dataframes

# LOAD two files first
df1 = pd.read_csv("titanic_info.csv")  # Load first dataset (passenger information)
df2 = pd.read_csv("titanic_ticket.csv")  # Load second dataset (ticket information)

# MERGE (JOIN USING COMMON COLUMN)
apple = pd.merge(df1, df2, on='passenger_id')  # Merge df1 and df2 using 'passenger_id' as the common key
# 'on' specifies the column that exists in both datasets and is used to match rows

print(apple.shape)  # Show total number of rows and columns after merging
print(apple.head(10))  # Show first 10 rows of the merged dataset

# NOTE: No need to reset index here because merge already creates a clean index
# Index will automatically run from 0 to n

# SAVE MERGED FILE to Python Project folder
apple.to_csv("titanic_merged.csv", index=False)  # Save the merged dataset as a new CSV file
print("Merged file saved successfully.")  # Confirm that the file was saved