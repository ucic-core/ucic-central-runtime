import gradio as gr

def create_ui():
    with gr.Blocks() as demo:
        gr.Markdown("# 🧠 UCIC Central Runtime UI")
        msg = gr.Textbox(label="Gửi prompt")
        out = gr.Textbox(label="Phản hồi")

        def reply(txt):
            return f"Bạn vừa gửi: {txt}"

        btn = gr.Button("Phản xạ")
        btn.click(reply, inputs=msg, outputs=out)

    return demo
