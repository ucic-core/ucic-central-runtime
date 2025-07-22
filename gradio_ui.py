import gradio as gr

def create_ui():
    with gr.Blocks() as demo:
        gr.Markdown("# 🧠 UCIC Central Runtime")
        gr.Textbox(label="Test chat phản xạ")
        gr.Button("Gửi")
    return demo
