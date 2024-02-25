"""Capstone Project"""

import spacy
import pandas as pd
from textblob import TextBlob


# 1. Implement a sentiment analysis model using spaCy

# Load small english spaCy model to enable natural language processing tasks
nlp = spacy.load('en_core_web_sm')


# 2. Preprocess the review data

# Define a helper function to remove stopwords from the data
def remove_stopwords(string):
    """Remove stopwords from data"""

    # Process the token and break it into individual words (tokens)
    doc = nlp(string)

    # Remove stopwords
    filtered_words = [token.text for token in doc if not token.is_stop]

    # Join the filtered words back together
    new_string = ' '.join(filtered_words)

    # return the new string without stopwords
    return new_string


# Import the data from the csv file
df = pd.read_csv('amazon_product_reviews.csv')

# Select the review text column and retrieve the data
reviews_data = df['reviews.text']

# Remove missing values
reviews_data = reviews_data.dropna()

# Convert the text to lowercase
reviews_data = reviews_data.str.lower()

# Remove punctuation, asterisks and parentheses
reviews_data = reviews_data.str.replace('.', '').replace(',', '').replace(
    '!', '').replace('*', '').replace('(', '').replace(')', '')

# Remove trailing whitespaces
reviews_data = reviews_data.str.strip()

# Remove stopwords
reviews_data = [remove_stopwords(review) for review in reviews_data]

# 3. Create a function for sentiment analysis
# that takes a product review as input and predicts its sentiment.


def predict_review_sentiment(review):
    """Predict the sentiment of a product review"""

    blob = TextBlob(review)

    # Use the polarity attribute to analyse the review and determine whether it
    # expresses a positive, negative, or neutral sentiment.
    polarity = blob.sentiment_assessments.polarity

    sentiment = ""
    # Get the sentiment of the review
    if polarity == 1:
        sentiment = 'very positive'
    elif polarity > 0:
        sentiment = 'positive'
    elif polarity == 0:
        sentiment = 'neutral'
    elif polarity == -1:
        sentiment = 'very negative'
    elif polarity < 0:
        sentiment = 'negative'

    # Return the sentiment of the review
    return (f"The sentiment of the review is {sentiment}, with a polarity of {round(polarity, 2)}.")


# 4. Test the sentiment analysis mode on sample product reviews

# Test 1
print(reviews_data[1])
# Printed cleaned review:
# great beginner experienced person bought gift loves

print(predict_review_sentiment(reviews_data[1]))
# Printed result of the sentiment analysis:
# The sentiment of the review is positive, with a polarity of 0.8.


# Test 2
print(reviews_data[222])
# Printed cleaned review:
# hoping use google launcher tablet locked change launcher lock screen cheap fine watching movies

print(predict_review_sentiment(reviews_data[222]))
# Printed result of the sentiment analysis:
# The sentiment of the review is positive, with a polarity of 0.41.


# Test 3
print(reviews_data[490])
# Printed cleaned review:
# good , hate , buy , sucks

print(predict_review_sentiment(reviews_data[490]))
# Printed result of the sentiment analysis:
# The sentiment of the review is negative, with a polarity of -0.13.


# Test 4
print(reviews_data[492])
# Printed cleaned review:
# think great product parents christmas gift

print(predict_review_sentiment(reviews_data[492]))
# Printed result of the sentiment analysis:
# The sentiment of the review is positive, with a polarity of 0.8.


# Test 5
print(reviews_data[3394])
# Printed cleaned review:
# problem charging kindle imac , travel need charger works perfectly

print(predict_review_sentiment(reviews_data[3394]))
# Printed result of the sentiment analysis:
# The sentiment of the review is very positive, with a polarity of 1.0.
