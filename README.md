# Sentiment and Word Guessing App

A simple Natural Language Processing (NLP) application built with Python, Hugging Face Transformers and Streamlit. The application allows users to analyse the sentiment of a sentence and predict missing words using pre-trained language models.

## Live Demo

[Open the Sentiment and Word Guessing App](https://sentiment-and-word-guessing-app-fxuerqhzgsyahztzrcawub5.streamlit.app)

## Project Overview

This project demonstrates how pre-trained NLP models can be integrated into a simple web application.

The application has two main features:

1. **Sentiment Analysis:** Analyses a sentence and classifies it as positive or negative.
2. **Missing Word Prediction:** Predicts possible words that can complete a sentence containing a `[MASK]` token.

## Features

### 1. Sentiment Analysis

- Accepts a sentence from the user.
- Uses a pre-trained sentiment analysis model.
- Classifies the sentence as POSITIVE or NEGATIVE.
- Displays the prediction score.

**Model:** `distilbert-base-uncased-finetuned-sst-2-english`

### 2. Missing Word Prediction

- Allows users to enter a sentence containing `[MASK]`.
- Predicts five possible replacement tokens.
- Displays the prediction scores as percentages.
- Uses progress bars to make the results easier to understand.

**Model:** `distilbert-base-uncased`

## Technologies Used

- Python
- Streamlit
- Hugging Face Transformers
- PyTorch
- Git and GitHub
- Streamlit Community Cloud

## Project Structure

```text
sentiment-and-word-guessing-app/
│
├── streamlit_app.py
├── sentiment.ipynb
├── requirements.txt
└── .gitignore
```

## Run the Application Locally

### 1. Clone the repository

```bash
https://github.com/NSJeremiah01/SENTIMENT-AND-WORD-GUESSING-APP
```

### 2. Open the project folder

```bash
cd sentiment-and-word-guessing-app
```

### 3. Install the dependencies

```bash
pip install streamlit torch transformers
```

### 4. Run the application

```bash
streamlit run streamlit_app.py
```

The application will open in your browser.

## How It Works

The application uses the Hugging Face `pipeline()` function to access pre-trained NLP models.

For sentiment analysis, the model examines the input sentence and returns a sentiment label and prediction score.

For missing word prediction, the fill-mask model examines the surrounding words and predicts possible replacements for the `[MASK]` token.

The models are loaded using Streamlit's `@st.cache_resource` decorator to avoid repeatedly loading them during application interactions.

## Limitations

- The sentiment model classifies text into positive or negative categories and may not fully understand sarcasm or complex expressions.
- The missing word model may return predictions that are grammatically possible but factually incorrect.
- Prediction scores indicate the model's confidence distribution over candidate tokens, not a guarantee that a prediction is correct.
- The application uses pre-trained models. I did not train these models from scratch.

## What I Learned

Through this project, I gained practical experience with:

- Using pre-trained NLP models.
- Working with Hugging Face Transformers pipelines.
- Understanding sentiment analysis and masked language modelling.
- Building interactive applications with Streamlit.
- Managing project files with Git and GitHub.
- Deploying a Python application using Streamlit Community Cloud.

## Project Status

Completed and deployed.

**Author:** Sunny  
**GitHub:** https://github.com/NSJeremiah01
