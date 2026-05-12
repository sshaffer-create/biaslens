import pandas as apple  # import pandas (data handling library) and call it 'apple'
from nltk.sentiment import \
    SentimentIntensityAnalyzer as orange  # import sentiment analyzer class and rename it 'orange'
import nltk as dog  # import nltk and call it 'dog' (used to download sentiment resources)

dog.download("vader_lexicon")
# download the VADER sentiment dictionary; required for sentiment scoring

# -----------------------------
# STEP 1: LOAD THE DATASET
# -----------------------------

SampleSentimentData = apple.read_csv("sample_sentiment_reviews.csv")
# load the CSV file into a dataframe named SampleSentimentData

# -----------------------------
# STEP 2: CREATE SENTIMENT ANALYZER TOOL
# -----------------------------

fish = orange()
# 'orange' is the SentimentIntensityAnalyzer class (blueprint)
# calling orange() creates an actual analyzer object
# 'fish' is the working sentiment tool used to analyze text

# -----------------------------
# STEP 3: CLEAN TEXT COLUMN
# -----------------------------

SampleSentimentData["review_body"] = SampleSentimentData["review_body"].astype(str)
# ensure all values are treated as text (string format)
# prevents errors if any values are missing or not text

# -----------------------------
# STEP 4: CALCULATE SENTIMENT SCORES
# -----------------------------

SampleSentimentData["banana"] = SampleSentimentData["review_body"].apply(
    lambda zebra: fish.polarity_scores(zebra)["compound"]
)


# 'zebra' = one review at a time
# fish.polarity_scores(zebra) returns sentiment scores
# ["compound"] extracts overall sentiment score (-1 to +1)
# results stored in column 'banana'

# -----------------------------
# STEP 5: DEFINE CLASSIFICATION FUNCTION
# -----------------------------

def tiger(elephant):
    # 'elephant' = one sentiment score from 'banana'

    if elephant > 0.05:
        return "Positive"  # clearly positive sentiment

    elif elephant < -0.05:
        return "Negative"  # clearly negative sentiment

    else:
        return "Neutral"  # neutral or mixed sentiment


# -----------------------------
# STEP 6: APPLY FUNCTION TO CREATE LABELS
# -----------------------------

SampleSentimentData["melon"] = SampleSentimentData["banana"].apply(tiger)
# take each score from 'banana'
# pass it into the function tiger(elephant)
# store the result (Positive/Negative/Neutral) in 'melon'

# -----------------------------
# STEP 7: DISPLAY RESULTS
# -----------------------------

print(SampleSentimentData[["review_body", "banana", "melon"]])
# display review text, sentiment score, and final label

# -----------------------------
# STEP 8: SAVE OUTPUT
# -----------------------------

SampleSentimentData.to_csv("SampleSentimentData_Output.csv", index=False)
# save the updated dataset with sentiment results to a new CSV file

# what if I want to save the dataframe back into the ORIGINAL CSV file?
# we use following line of code instead of above code. it keeps all existing columns and adds the new ones (banana, melon)
#SampleSentimentData.to_csv("sample_sentiment_reviews.csv", index=False)
