from transformers import pipeline
import gradio as gr

# Load free model from Hugging Face
chatbot = pipeline("text2text-generation", model="google/flan-t5-small")

# Define the chatbot function
def chat(message):
    prompt = f"Chat with me: {message}"
    response = chatbot(prompt, max_length=100)[0]["generated_text"]
    return response

# Create a simple chat UI
gr.ChatInterface(fn=chat).launch(share=True)
