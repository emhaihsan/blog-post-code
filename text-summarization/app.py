
import json
import requests
import gradio as gr
from dotenv import dotenv_values

config = dotenv_values(".env")
hf_api_key = config['HF_API_KEY']


API_URL = "https://api-inference.huggingface.co/models/sshleifer/distilbart-cnn-12-6"

def get_completion(inputs, parameters=None,ENDPOINT_URL=API_URL): 
    headers = {
      "Authorization": f"Bearer {hf_api_key}",
      "Content-Type": "application/json"
    }
    data = { "inputs": inputs }
    if parameters is not None:
        data.update({"parameters": parameters})
    response = requests.request("POST",
                                ENDPOINT_URL, headers=headers,
                                data=json.dumps(data)
                               )
    return json.loads(response.content.decode("utf-8"))

# Define summarization function

def summarize(input):
    output = get_completion(input)
    return output[0]['summary_text']

# Define the Gradio interface
interface = gr.Interface(fn=summarize, 
                    inputs=[gr.Textbox(label="Text to summarize", lines=6)],
                    outputs=[gr.Textbox(label="Result", lines=3)],
                    title="Text summarization with distilbart-cnn",
                    description="Summarize any text using the `shleifer/distilbart-cnn-12-6` model under the hood!"
                   )
# Launch the interface
interface.launch()
