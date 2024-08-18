# Sentiment Analysis Web App with GPT-4-turbo and Streamlit

This project is a simple web application that performs sentiment analysis on user-provided text using the GPT model from OpenAI. The web interface is built using Streamlit, a powerful and easy-to-use Python framework for creating interactive web apps.

## Features

- **Sentiment Analysis**: Classifies the sentiment of input text as Positive, Negative, or Neutral.
- **Interactive UI**: A clean and intuitive interface built with Streamlit.
- **Real-time Feedback**: Provides immediate sentiment analysis with visual feedback (green for positive, red for negative, yellow for neutral).
- **Error Handling**: Detects and handles missing or incorrect API keys and other potential issues.

## Usage

1. Run the application:

   ```bash
   streamlit run app.py
   ```

2. Open your web browser and go to the local url given.

3. Enter your OpenAI API key in the sidebar.

4. Input the text you want to analyze in the text area.

5. Click the "Analyze Sentiment" button to see the results.

## Project Structure

```
.
├── app.py                 # The Streamlit UI code
├── gpt.py                 # The sentiment analysis logic using OpenAI API
├── requirements.txt       # Required Python packages
└── README.md              # Project documentation (this file)
```

## Code Explanation

### `app.py`

This file contains the code for the Streamlit interface. It handles user input, API key validation, and displaying the sentiment analysis results with appropriate visual feedback.

### `gpt.py`

This file contains the logic for interacting with the OpenAI model. It defines the `get_sentiment` function, which sends the user input to the model and returns the sentiment classification.

## Error Handling

- **Missing API Key**: The app will prompt you to enter your API key if it's missing.
- **Invalid API Key**: The app will notify you if the API key is invalid.

## Contact

If you have any questions, feel free to reach out:

- Email: emhihsan@gmail.com
- LinkedIn: [Muhammad Ihsan](https://www.linkedin.com/in/emhaihsan/)
