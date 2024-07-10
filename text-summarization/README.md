# Text Summarization with DistilBART-CNN

This project demonstrates how to create a text summarization application using the `sshleifer/distilbart-cnn-12-6` model from Hugging Face. The application is built using Python, Gradio for the interface, and the Hugging Face Inference API for text summarization.

## Requirements

- Python 3.6+
- Gradio
- Requests
- Python-dotenv
- Hugging Face API Key

## Usage

1. Run the script to start the Gradio interface:

```bash
python app.py
```

2. Open the provided local URL in your web browser to access the interface.

3. Enter the text you want to summarize in the "Text to summarize" textbox and click the "Submit" button.

4. The summarized text will appear in the "Result" textbox.

## Project Structure

- `app.py`: Main script that contains the code to set up and launch the Gradio interface.
- `.env`: Environment file to store the Hugging Face API key.
- `requirements.txt`: List of required Python packages.

## Code Explanation

- The script starts by importing necessary libraries: `json`, `requests`, `gradio`, and `dotenv`.
- The Hugging Face API key is loaded from the `.env` file.
- The `get_completion` function sends a request to the Hugging Face Inference API to get the summary of the input text.
- The `summarize` function processes the input text and retrieves the summarized text.
- A Gradio interface is defined with a textbox for input and output, along with a title and description.
- The Gradio interface is launched using `interface.launch()`.

## Acknowledgments

- [Hugging Face](https://huggingface.co/) for providing the API and models.
- [Gradio](https://gradio.app/) for creating an easy-to-use interface library.

Feel free to customize and extend this project according to your needs. Happy summarizing!

## License

This project is licensed under the MIT License.

## Contact

For any questions or suggestions, feel free to contact me at emhihsan@gmail.com.