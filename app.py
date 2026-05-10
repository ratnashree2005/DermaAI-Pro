!pip install -q gradio google-genai

import gradio as gr
from google import genai

# Gemini API Key
client = genai.Client(api_key="AIzaSyAK6HszdXz3-1YmpMDj3IixARJKJhO2xIQ")

def generate_response(image, text_prompt):

    uploaded_file = client.files.upload(file=image)

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[uploaded_file, text_prompt],
    )

    return response.text

# Custom Gradio UI
with gr.Blocks() as demo:

    gr.Markdown("# Gemini Image + Text App")

    with gr.Row():
        image_input = gr.Image(type="filepath", label="Upload Image")

    text_input = gr.Textbox(
        label="Enter Prompt",
        placeholder="Describe this image..."
    )

    output = gr.Textbox(
        label="Gemini Response",
        lines=15,          # Increased visible height
        max_lines=25,      # Allows bigger expansion
        show_copy_button=True
    )

    submit_btn = gr.Button("Generate")

    submit_btn.click(
        fn=generate_response,
        inputs=[image_input, text_input],
        outputs=output
    )

demo.launch(share=True)