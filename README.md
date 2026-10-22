# SentimentScope — Text Sentiment Analysis System

SentimentScope is a beginner-friendly Natural Language Processing (NLP) web application built with Python, Streamlit, and TextBlob. It classifies a piece of English text as **Positive**, **Negative**, or **Neutral**, and displays polarity, subjectivity, and basic text statistics.

## Features

- Sentiment classification: Positive, Negative, or Neutral
- Polarity score from `-1` (negative) to `+1` (positive)
- Subjectivity score from `0` (objective) to `1` (subjective)
- Example inputs for quick testing
- Word, character, sentence, and unique-word counts
- Most common words display
- Simple interactive Streamlit interface
- No API key, database, or external service required

## Tech stack

- Python
- Streamlit
- TextBlob
- Regular expressions and Python collections

## Project structure

```text
Sentiment_Analysis_System/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── LICENSE
├── sample_texts/
│   └── examples.txt
└── tests/
    └── test_sentiment.py
```

## Run locally

### 1. Install Python

Use Python 3.10 or newer. Python 3.12 is a good choice.

### 2. Download or clone this repository

```bash
git clone https://github.com/YOUR-USERNAME/Sentiment_Analysis_System.git
cd Sentiment_Analysis_System
```

If you downloaded the ZIP, extract it and open a terminal in the extracted folder.

### 3. Create a virtual environment (recommended)

**Windows:**
```powershell
py -3.12 -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Start the application

```bash
streamlit run app.py
```

Streamlit will show a local URL, usually `http://localhost:8501`. Open it in your browser.

## How it works

1. The user enters a sentence, review, or paragraph.
2. TextBlob calculates sentiment polarity and subjectivity.
3. The app maps polarity to a label:
   - Polarity greater than `0.05`: Positive
   - Polarity less than `-0.05`: Negative
   - Otherwise: Neutral
4. The app displays the result and simple text statistics.

## Example

Input:

> I absolutely love this product. It is easy to use and works wonderfully!

The expected classification is **Positive**. Exact scores depend on the text and TextBlob version.

## Limitations

- The built-in sentiment analyzer is intended primarily for English.
- Sarcasm, idioms, slang, negation, and context can lead to incorrect predictions.
- A neutral result does not mean the text has no emotion; it means the score falls near zero.
- This is an educational demo, not a system for making high-stakes decisions.

## Run the tests

```bash
python -m unittest discover -s tests -v
```

## Deploy on Streamlit Community Cloud

1. Push this project to a public GitHub repository.
2. Sign in to Streamlit Community Cloud.
3. Select **Create app** and choose your repository and branch.
4. Set the main file path to `app.py`.
5. Deploy. The platform installs packages listed in `requirements.txt`.

## GitHub upload

Create a new repository named `Sentiment_Analysis_System` on GitHub. Do not initialize it with a README if you plan to push this existing project.

From the project folder:

```bash
git init
git add .
git commit -m "Add SentimentScope text sentiment analyzer"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/Sentiment_Analysis_System.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username.

## License

This project is released under the MIT License. See `LICENSE`.
