# Giao diện Gradio cơ bản
import gradio as gr

def greet(name): return f'Xin chào, {name}'
gr.Interface(fn=greet, inputs='text', outputs='text').launch()