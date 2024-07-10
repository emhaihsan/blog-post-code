# Image Captioning with BLIP

This project showcases an application for image captioning using the `Salesforce/blip-image-captioning-base` model from Hugging Face. The application is built with Python, Gradio for the user interface, and the Hugging Face Inference API for generating captions.

## Requirements

- Python 3.6+
- Gradio
- Requests
- Python-dotenv
- Pillow

## Usage

1. Run the script to start the Gradio interface:

```bash
python app.py
```

2. Open the provided local URL in your web browser to access the interface.

3. Upload an image by dragging and dropping or by clicking the "Upload image" button.

4. The caption for the uploaded image will appear in the "Caption" textbox.

## Project Structure

- `app.py`: Main script that contains the code to set up and launch the Gradio interface.
- `example/`: Directory containing example images.

## Code Explanation

- The script imports necessary libraries: `io`, `base64`, `json`, `requests`, `gradio`, and `dotenv`.
- The Hugging Face API key is loaded from the `.env` file.
- The `get_completion` function sends a request to the Hugging Face Inference API to get the caption for the input image.
- The `image_to_base64_str` function converts a PIL image to a base64-encoded string.
- The `captioner` function processes the uploaded image and retrieves the generated caption.
- A Gradio interface is defined with an image input and a textbox output, along with a title, description, and example images.
- The Gradio interface is launched using `demo.launch()`.

## Acknowledgments

- [Hugging Face](https://huggingface.co/) for providing the API and models.
- [Gradio](https://gradio.app/) for creating an easy-to-use interface library.

Feel free to customize and extend this project according to your needs. Happy captioning!

## License

This project is licensed under the MIT License.

## Contact

For any questions or suggestions, feel free to contact me at [your-email@example.com].