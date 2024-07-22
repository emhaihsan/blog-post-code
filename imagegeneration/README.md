# Image Generation with Stable Diffusion

This project leverages the Stable Diffusion model from Hugging Face to generate images based on text prompts. The project uses Gradio to create a user-friendly interface for interacting with the model.

## Features

- **Text Prompt Input**: Enter any text prompt to generate an image.
- **Inference Steps**: Control the number of steps the model takes to generate the image.
- **Guidance Scale**: Adjust how much the text prompt influences the result.
- **Custom Dimensions**: Set the width and height of the generated image.


## Setup

Set up your Hugging Face API key:
  - Create a `.env` file in the root directory of your project.
  -  Add your Hugging Face API key to the `.env` file:
    ```
    HF_API_KEY=your_huggingface_api_key
    ```

## Usage

To run the application, use the following command:
```bash
python app.py
