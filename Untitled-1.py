# this is were I will be showing the ai that I will make 
# 1st I need to import ,the important files 
# such as the nlp library and scholarly
# Import the necessary libraries 
import nltk
import webbrowser
from nltk.stem import WordNetLemmatizer
import scholarly
import requests
from bs4 import BeautifulSoup

# Download nltk resources
nltk.download('punkt') 
nltk.download('wordnet')


# Create lemmatizer instance
lemmatizer = WordNetLemmatizer()  

# Function to preprocess text
# Function to preprocess text
def preprocess(text):
    # Tokenize words and lemmatize them
    words = [lemmatizer.lemmatize(word) for word in nltk.word_tokenize(text)]
    # Join the lemmatized words into a single string
    processed_text = ' '.join(words)
    return processed_text


# Function for academic search
def academic_search(query):
    try:
        # Perform search on Google Scholar
        url = f"https://scholar.google.com/scholar?q={query}"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            results = soup.find_all('div', class_='gs_r gs_or gs_scl')
            if results:
                # Open the search results page in the default web browser
                webbrowser.open(url)
                print("Search results opened in your default browser.")
                # Print out some key info from each result
                print(f"Relevant results for '{query}':")
                for result in results:
                    title = result.find('h3', class_='gs_rt').text.strip()
                    authors = result.find('div', class_='gs_a').text.strip()
                    year = result.find('div', class_='gs_a').text.split('-')[-1].strip()
                    link = result.find('a')['href']
                    print("Title:", title)
                    print("Authors:", authors)
                    print("Year:", year)
                    print("Link:", link)
                    print()
            else:
                print("No academic papers found for this query.")
        else:
            print("Failed to retrieve search results.")
    except Exception as e:
        print("An error occurred:", e)



# Define explanations for keywords
explanations = {
    "nlp": "NLP (Natural Language Processing) is a field of artificial intelligence focused on the interaction between computers and humans through natural language.",
    "scholarly": "Scholarly is a Python library for scholarly research. It allows you to search for academic papers and retrieve their metadata.",
    "lemmatizer": "A lemmatizer is a tool used in natural language processing to reduce words to their base or root form, called a lemma.",
    # Add more explanations as needed
}

# Function to provide explanations
def provide_explanation(query):
    query = query.lower()
    for keyword, explanation in explanations.items():
        if keyword in query:
            return explanation
    return "I'm sorry, I don't have an explanation for that."


def conduct_quiz():
    print("Let's start the quiz and generate flashcards!")
    flashcards = []

    # Ask each question and generate flashcards
    for question, answer in quiz_questions.items():
        # Ask the question
        user_answer = input(question + " ")

        # Add flashcard
        flashcard = {
            "prompt": question,
            "answer": answer
        }
        flashcards.append(flashcard)

        # Check user's answer
        if user_answer.lower() == answer.lower():
            print("Correct!")
        else:
            print(f"Sorry, the correct answer is {answer}.")

    print("Flashcards generated successfully!")
    return flashcards




# Main dialog function    
def chat():
    print("Hello, I'm ResearchBot! How can I help you with your schoolwork today?")
    
    while True:
        text = input("You: ")
        
        # Preprocess text
        text = preprocess(text)   
        
        # Classify intent using keywords
        if 'search' in text:
            # Extract search query
            query = text.split('search')[-1]
            academic_search(query)
        
        elif 'explain' in text:
            # Provide explanation
            query = text.split('explain')[-1]
            explanation = provide_explanation(query)
            print("ResearchBot:", explanation)
        
        
        elif 'quiz' in text:
            # Start the quiz and generate flashcards
            flashcards = conduct_quiz()
            print("Generated Flashcards:")
            for flashcard in flashcards:
                print("Prompt:", flashcard["prompt"])
                print("Answer:", flashcard["answer"])
                print()
        
        
        else:
            print("ResearchBot: I'm sorry, I don't understand. Please ask me a question about research, assignments, or studying!")


# Start chatbot      
chat()
