from flask import Flask, render_template
from threading import Thread
import tkinter as tk
from chatbot import chat

app = Flask(__name__)

def start_chat():
    chat()

def create_tkinter_gui():
    root = tk.Tk()
    root.title("ResearchBot")

    label = tk.Label(root, text="Welcome to ResearchBot", font=("Arial", 16))
    label.pack(pady=20)

    button = tk.Button(root, text="Start Chat", command=start_chat, font=("Arial", 14))
    button.pack(pady=10)

    root.mainloop()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_chat')
def start_chat_route():
    # Start the Tkinter GUI in a separate thread
    chat_thread = Thread(target=create_tkinter_gui)
    chat_thread.start()
    return 'Chat started'

if __name__ == '__main__':
    app.run(debug=True)
