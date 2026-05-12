

################################      ANOVA     ########################

# Null Hypothesis (H₀): # The mean age of passengers is the same across all passenger classes (1st, 2nd, 3rd).
# μ1 = μ2 = μ3

# Alternative Hypothesis (Ha): # At least one passenger class has a different mean age.
# Not all group means are equal

from scipy.stats import f_oneway  # Import ANOVA function

# Select ages for each passenger class and remove missing values
class1 = titanic[titanic['pclass'] == 1]['age'].dropna()
class2 = titanic[titanic['pclass'] == 2]['age'].dropna()
class3 = titanic[titanic['pclass'] == 3]['age'].dropna()

# Perform one-way ANOVA test
f_stat, p_value = f_oneway(class1, class2, class3)

# Output results
print("F-statistic for ANOVA:", f_stat)
print("P-value for ANOVA:", p_value)

###################### SIMPLE LINEAR REGRESSION #############################

# Null Hypothesis (H₀): # There is no linear relationship between age and fare.
# → The slope (β₁) = 0

# Alternative Hypothesis (H₁): # There is a linear relationship between age and fare.
# → The slope (β₁) ≠ 0

from sklearn.linear_model import LinearRegression  # Import Linear Regression model
from sklearn.model_selection import train_test_split  # For splitting data
from sklearn.metrics import r2_score, mean_squared_error  # For evaluation

# Select variables and remove missing values
data = titanic[['age', 'fare']].dropna()
# We keep only age (X) and fare (y), and remove rows with missing values

# Define independent (X) and dependent (y) variables
X = data[['age']]   # Feature (must be 2D)
y = data['fare']    # Target variable

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
# 80% for training, 20% for testing

# Create Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)
# Model learns relationship between age and fare

# Make predictions on test data
y_pred = model.predict(X_test)

# Evaluate model performance
print("R² score:", r2_score(y_test, y_pred))
# Shows how much variance in fare is explained by age

print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
# Measures prediction error (lower is better)

# Print model parameters
print("Slope (coefficient):", model.coef_)
# Change in fare for one unit increase in age

print("Intercept:", model.intercept_)
# Predicted fare when age = 0

######################## Logistic REGRESSION    #################3
#Null Hypothesis (H₀): Passenger class, fare, and age have no significant relationship with survival;
# they do not affect the likelihood of surviving the Titanic disaster.
# Alternative Hypothesis (Ha): # Passengers with higher class (lower pclass number), higher fare, and younger age
#are more likely to survive the Titanic disaster.

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

# Select features and clean missing values
features = titanic[['pclass', 'age', 'fare']].dropna()

# Align target variable with cleaned features
target = titanic.loc[features.index, 'survived']

# --- Split into training and testing sets ---
#Splitting into Train, Testing, is required to ensure that the model is evaluated on unseen data,
# so we can check whether it truly learns patterns rather than just memorizing the training data.
# 80% training, 20% testing
#random_state=42 sets a fixed random seed so that the train–test split is the same every time you run the code.
X_train, X_test, y_train, y_test = train_test_split(
    features, target, test_size=0.2, random_state=42
)

# Create model
model = LogisticRegression()

# --- Training ---
model.fit(X_train, y_train)

# --- Testing (prediction on unseen data) ---
y_pred = model.predict(X_test)

# --- Evaluation ---
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# --- Model interpretation ---
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)