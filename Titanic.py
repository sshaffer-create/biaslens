# Setup: Import Libraries and Load Dataset ---
import pandas as pd  # pandas is used to read, store, clean, and analyze table-like data such as CSV or Excel files
import numpy as np  # numpy is used for numerical operations, arrays, and mathematical functions
import matplotlib.pyplot as plt  # matplotlib.pyplot is used to create basic charts and graphs
import seaborn as sns  # seaborn is used to create cleaner and more attractive statistical visualizations

titanic = pd.read_csv("titanic.csv")  # Load the Titanic CSV file into a pandas DataFrame named titanic
# titanic = pd.read_excel("titanic.xlsx")  # Use this instead if your Titanic file is in Excel format
#if your file isn't in the same folder where your .py file is, we do the following:
#titanic = pd.read_csv("C:/Users/Shwadhin Sharma/Downloads/titanic.csv")  # Load file from Downloads folder
#if there are multiple worksheet in the excel file, you can import both in the following way:
#titanic_sheet1 = pd.read_excel("titanic.xlsx", sheet_name="Sheet1")  # Load Sheet1 or the sheet name into a dataframe
#titanic_sheet2 = pd.read_excel("titanic.xlsx", sheet_name="Sheet2")  # Load Sheet2 or the sheet name into a dataframe

#  Data Overview and Sampling ---
print(titanic.shape)  # Prints (rows, columns)
print(titanic.head(5))  # Print the first 5 rows of the dataset to quickly inspect the data
print(titanic.tail(5))  # Print the last 5 rows of the dataset
print(titanic.sample(10))  # Print 10 random rows from the dataset

# Indexing Examples with iloc (integer location) ---
print(titanic.iloc[0:5, :])  # First 5 rows, all columns
print(titanic.iloc[:, :])  # All rows, all columns
print(titanic.iloc[5:, :5])  # From row 5 onward, first 5 columns

# --- 4. Data Types and Null Values ---
print(titanic.info())  # Full info: data types, non-null counts
print(titanic.isnull().sum())  # Total null values per column
print(titanic.dtypes)  # Show the data type of each column, such as int, float, or object
print(titanic.describe())  # Show summary statistics for numeric columns such as count, mean, std, min, and max
print(titanic.describe(include='object'))  # Show summary information for categorical/text columns

print(titanic['survived'].value_counts())  # Count how many passengers survived and how many did not
print(titanic['sex'].value_counts())  # Count how many males and females are in the dataset
print(titanic['pclass'].value_counts())  # Count how many passengers are in each ticket class

#--------- Basic descriptive statistics ------
print(titanic['age'].mean())  # Print the average age of passengers
print(f"Mean age: {titanic['age'].mean():.2f}") #it prints the average age neatly formatted to 2 decimals.
print(titanic['age'].median())  # Print the median age of passengers
print(titanic['age'].mode())  # Print the most common age value or values
print(titanic['age'].min())  # Print the minimum age in the dataset
print(titanic['age'].max())  # Print the maximum age in the dataset

print(titanic.isnull().sum())  # Show how many missing values exist in each column

#-----------Scatter plot----------------
x = titanic['age']  # Store the age column in variable x
y = titanic['fare']  # Store the fare column in variable y
scatter_data = titanic[['age', 'fare']].dropna()  # Keep only rows where both age and fare are not missing
plt.xlabel('Age')  # Label the x-axis as Age
plt.ylabel('Fare')  # Label the y-axis as Fare
plt.title('Scatter Plot of Age vs Fare')  # Add a title to the scatter plot
plt.scatter(scatter_data['age'], scatter_data['fare'])  # Create a scatter plot of age and fare
plt.show()  # Display the scatter plot

# ---  Count Plot: Survival Count ---
sns.countplot(x="survived", data=titanic)
plt.title("Survival Count (0 = No, 1 = Yes)")
plt.xlabel("Survived")
plt.ylabel("Passenger Count")
plt.pause(0.001)
input("Press Enter to close the plot...")
plt.close()

# --- Count Plot: Survival by Gender ---
sns.countplot(x="sex", hue="survived", data=titanic)
plt.title("Survival by Gender")
plt.xlabel("Sex")
plt.ylabel("Passenger Count")
#plt.pause(0.001)
input("Press Enter to close the plot...")
plt.close()

# --- Visualization using seaborn factorplot (now called catplot in newer versions) ---
# Plot 1: Survival rate vs Family_Size
# x-axis: Family_Size (0, 1, 2, etc.)
# y-axis: survived (0 = died, 1 = survived)
# This shows the average survival rate for each family size group
sns.factorplot(x='Family_Size', y='survived', data=titanic)

# Plot 2: Survival rate vs Alone
# x-axis: Alone (0 = not alone, 1 = alone)
# y-axis: survived
# This compares survival probability of people traveling alone vs with family
sns.factorplot(x='Alone', y='survived', data=titanic)

#----------Histogram for Age---------
age_data = titanic['age'].dropna()  # Remove missing values from age before making a histogram
plt.xlabel('Age')  # Label the x-axis as Age
plt.ylabel('Frequency')  # Label the y-axis as Frequency
plt.title('Histogram of Age')  # Add a title to the histogram
plt.hist(age_data, bins=15)  # Create a histogram of age with 15 bins
plt.show()  # Display the histogram

#----------Histogram for Fare---------
fare_data = titanic['fare'].dropna()  # Remove missing values from fare before making a histogram
plt.xlabel('Fare')  # Label the x-axis as Fare
plt.ylabel('Frequency')  # Label the y-axis as Frequency
plt.title('Histogram of Fare')  # Add a title to the histogram
plt.hist(fare_data, bins=15)  # Create a histogram of fare with 15 bins
plt.show()  # Display the histogram

#---------- Bar Chart for Survival---------
survival_counts = titanic['survived'].value_counts()  # Count the number of passengers in each survival group
plt.xlabel('Survived')  # Label the x-axis as Survived
plt.ylabel('Count')  # Label the y-axis as Count
plt.title('Bar Chart of Survival Counts')  # Add a title to the bar chart
plt.bar(survival_counts.index.astype(str), survival_counts.values)  # Create a bar chart for survival counts
plt.show()  # Display the bar chart

#---------- Bar Chart for Sex---------
sex_counts = titanic['sex'].value_counts()  # Count the number of passengers by sex
plt.xlabel('Sex')  # Label the x-axis as Sex
plt.ylabel('Count')  # Label the y-axis as Count
plt.title('Bar Chart of Passenger Sex')  # Add a title to the bar chart
plt.bar(sex_counts.index, sex_counts.values)  # Create a bar chart for male and female counts
plt.show()  # Display the bar chart

#---------- Box plot---------
sns.boxplot(x='survived', y='age', data=titanic)  # Create a boxplot to compare age distribution by survival group
plt.xlabel('Survived')  # Label the x-axis as Survived
plt.ylabel('Age')  # Label the y-axis as Age
plt.title('Boxplot of Age by Survival Status')  # Add a title to the boxplot
plt.show()  # Display the boxplot

#-------- Count Plot ----------
sns.countplot(x='pclass', hue='survived', data=titanic)  # Create a count plot showing passenger class split by survival status
plt.xlabel('Passenger Class')  # Label the x-axis as Passenger Class
plt.ylabel('Count')  # Label the y-axis as Count
plt.title('Passenger Class by Survival')  # Add a title to the count plot
plt.show()  # Display the count plot

#------------Correlation ---------------
correlation_data = titanic[['survived', 'pclass', 'age', 'sibsp', 'parch', 'fare']].corr()  # Compute correlation among selected numeric columns
sns.heatmap(correlation_data, annot=True, cmap='coolwarm')  # Create a heatmap of the correlation matrix with values shown
plt.title('Correlation Heatmap')  # Add a title to the heatmap
plt.show()  # Display the heatmap