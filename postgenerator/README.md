# Social Media Post Generator

This project is a **Streamlit** application that generates social media posts using OpenAI's GPT model. The app allows users to input their desired topic and customize the post according to the platform (Facebook, Instagram, Twitter, LinkedIn), creativity level, post length, and the inclusion of hashtags and emojis.

## Features

- **Platform Selection**: Choose from popular platforms like Facebook, Instagram, Twitter, and LinkedIn.
- **Creativity Level (Temperature)**: Adjust the creativity of the generated post by setting the temperature value.
- **Post Length**: Choose between Short, Medium, and Long posts.
- **Hashtags and Emojis**: Optionally include or exclude hashtags and emojis in the generated posts.
- **API Key Protection**: Securely input your OpenAI API key to generate posts.

## Usage

1. **Enter OpenAI API Key**: Input your OpenAI API key in the sidebar.
2. **Configure the Post**: Select the platform, adjust the creativity level, choose the post length, and decide whether to include hashtags and emojis.
3. **Generate Post**: Click the "Generate Post" button to create a custom social media post based on the input parameters.
4. **Review and Use**: The generated post will be displayed on the main page, ready for you to copy and use on your social media.

## Error Handling

- If an invalid API key is provided, an error message will be displayed.
- If any other error occurs during post generation, the error message will be shown to the user.
