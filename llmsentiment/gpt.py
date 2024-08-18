import openai

def get_sentiment(text, user_api_key):
    try:
        client = openai.OpenAI(api_key=user_api_key)
        prompt = f"Analyze the sentiment of the following text, and classify it as positive, negative, or neutral:\n\n{text}"
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a sentiment analyzer, your must answer with only positive, negative, or neutral"},
                {"role": "user", "content": prompt}
            ],
            max_tokens=140,
            temperature=0.7,
        )
        sentiment = response.choices[0].message.content
        return sentiment
    except openai.AuthenticationError:
        return "Invalid API key"
    except Exception as e:
        return str(e)
