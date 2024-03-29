# Capstone Project

## Table of Contents:

- [Description](#description)
- [Aim](#aim)
- [Steps](#steps)
- [Tech stack](#tech-stack)
- [Running the project locally](#running-the-project-locally)
  * [Installation](#installation)
  * [Usage](#usage)
    + [Usage example](#-usage-example--)
- [Credits](#credits)


## Description

The aim of the Capstone Project was to categorise and research Natural Language Processing (NLP) applications.

Within the project a dataset containing reviews of Amazon products is cleaned for usage within a NLP model.
Finally sentiment analysis using a NLP model is performed.

The **Capstone Project** was completed for the **CoGrammar Skills Bootcamp in Data Science (Fundamentals)**.

## Aim

The aim of the project was to investigate how performant and accurate the used NLP was for
sentiment analysis of reviews.


## Steps

Steps performed within this project were:

1. Loading of small english spaCy model for natural language processing tasks
2. Import of reviews data
3. Cleaning of reviews data
4. Implementation of a function for sentiment analysis (`predict_review_sentiment`) on product reviews
5. Testing of the `predict_review_sentiment` function on reviews from the cleaned data set


## Tech stack

- [`python`](https://www.python.org/): overall programming and processing of data
- [`pandas`](https://pandas.pydata.org/): importing and reading of data
- [`spacy`](https://spacy.io/): tokenization and cleaning of data
- [`textblob`](https://textblob.readthedocs.io/en/dev/): sentiment analysis of data


## Running the project locally

### Installation

To run the project locally, install the required libraries (mentioned under Tech stack)
and run the code within a Python environment.

### Usage

Add new test cases when desiring to check further reviews.

To do so, call the `predict_review_sentiment` function with a selected review.
Print out the result to judge the accuracy of the sentiment analysis.

#### _Usage example:_

```
# Test case
print(reviews_data[1])
# Printed cleaned review:
# great beginner experienced person bought gift loves

print(predict_review_sentiment(reviews_data[1]))
# Printed result of the sentiment analysis:
# The sentiment of the review is positive, with a polarity of 0.8.
```

<img width="591" alt="capstone" src="https://github.com/BeauClancy/finalCapstone/assets/82422556/d04fc290-eb4c-4a05-884d-c7636cc52bbc">


## Credits

The used data set was provided by [Datafiniti's Product Database via Kaggle](https://www.kaggle.com/datasets/datafiniti/consumer-reviews-of-amazon-products).

The project idea was provided by Hyperion Dev within the framework of the
**CoGrammar Skills Bootcamp in Data Science (Fundamentals)**.
