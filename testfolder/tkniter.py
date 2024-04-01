import tkinter as tk
from chatbot import chat

# Example chat function
def chat(query):
    # This is where you'd process the query and generate a response.
    # For demonstration, it just echoes the query.
    return "Response to your query: " + query

# Function to be called when the submit button is pressed
def submit_query():
    query = entry.get()  # Get the text from the Entry widget
    response = chat(query)  # Call the chat function with the query
    response_label.config(text=response)  # Update the Label with the response
    print(response)  # Print response to console
    print(query)
# Setting up the Tkinter window
root = tk.Tk()
root.title("Query Chat")

# Entry widget for the user to type their query
entry = tk.Entry(root, width=50)
entry.pack(padx=10, pady=10)

# Button that calls submit_query when pressed
submit_button = tk.Button(root, text="Submit", command=submit_query)
submit_button.pack(pady=5)

# Label to display the response
response_label = tk.Label(root, text="Response will be shown here.", wraplength=400)
response_label.pack(padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()