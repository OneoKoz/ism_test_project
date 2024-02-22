import os
import gradio as gr
from model import Model

model = Model()

def generate(prompt, neg_prompt, progress=gr.Progress(track_tqdm=True)):
    if not prompt:
        gr.Warning('prompt textbox conn`t be empty')
        return
    image = model.create_image(prompt, neg_prompt=neg_prompt)
    return image


with gr.Blocks() as demo:
    gr.Markdown(
    """
    # ISM GEN IMG
    """)
    with gr.Column():
        prompt_input = gr.Textbox(label='prompt')
        neg_prompt_input = gr.Textbox(label='neg_prompt')
        btn_generate = gr.Button("generate")
        image_output = gr.Image()

    btn_generate.click(generate, 
                       [prompt_input, neg_prompt_input], 
                       [image_output])


if __name__ == "__main__":
    demo.launch(server_name=os.environ['GRADIO_SERVER_PATH'], server_port=int(os.environ['GRADIO_SERVER_PORT']))
