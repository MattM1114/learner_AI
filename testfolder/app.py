import tkinter as tk
from chatbot import chat

def start_chat():
    chat()

def main():
    root = tk.Tk()
    root.title("ResearchBot")
    
    # Create labels and button
    label = tk.Label(root, text="Welcome to ResearchBot")
    label.pack(pady=10)
    
    button = tk.Button(root, text="Start Chat", command=start_chat)
    button.pack(pady=5)
    
    # Run the application
    root.mainloop()



