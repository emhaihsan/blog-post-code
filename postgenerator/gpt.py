import openai

def generate_post(api_key, platform, topic, temperature, length, use_hashtags, use_emojis):
    try:
        client = openai.OpenAI(api_key=api_key)
        prompt = f"Generate a {length} social media post for {topic} in {platform}."
        
        if use_hashtags:
            prompt += " Include relevant hashtags."
        else:
            prompt += " Do not include hashtags."
        if use_emojis:
            prompt += " Include appropriate emojis."
        else:
            prompt += " Do not include emojis."
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a social media expert with 20 years experience on Cupywriting"},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            temperature=temperature  # Adding temperature parameter
        )
        post = response.choices[0].message.content
        return post
    except openai.AuthenticationError:
        return "Invalid API key"
    except Exception as e:
        return str(e)
