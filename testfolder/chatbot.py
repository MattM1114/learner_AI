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
from nltk.tokenize import sent_tokenize
from datetime import datetime
import math
import sympy as sp
from sympy import Symbol


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
    current_year = datetime.now().year
    search_years_range = f"{current_year-4}-{current_year}"
    
    try:
        # Perform search on Google Scholar
        url = f"https://scholar.google.com/scholar?as_ylo={current_year-4}&q={query}"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            results = soup.find_all('div', class_='gs_ri')[:10]  # Get top 10 results   
            print(f"Top 10 relevant results for '{query}' from {search_years_range}:")
            for index, result in enumerate(results, start=1):
                title_element = result.find('h3', class_='gs_rt')
                title = title_element.text.strip() if title_element else "No title found"
                link_element = title_element.find('a') if title_element else None
                link = link_element['href'] if link_element else "No link available"
            # Extract authors
                abstract_element = result.find('div', class_='gs_rs')
                abstract = abstract_element.text.strip() if abstract_element else "No abstract available"
                print(f"\nArticle {index}:")
                print(f"Title: {title}")
                print(f"Abstract: {abstract}")
                print(f"Url: {link}")
        else:
            print("Failed to retrieve search results.")
    except Exception as e:
        print(f"An error occurred: {e}")

import requests
from bs4 import BeautifulSoup

def explain(query):
    try:
        # Perform search on Google Scholar
        url = f"https://scholar.google.com/scholar?q={query}"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            results = soup.find_all('div', class_='gs_r gs_or gs_scl')
            if results:
                # Get the top result
                top_result = results[0]
                
                # Extract details
                title = top_result.find('h3', class_='gs_rt').text.strip()
                authors = top_result.find('div', class_='gs_a').text.strip()
                year = top_result.find('div', class_='gs_a').text.split('-')[-1].strip()
                link = top_result.find('a')['href']
                
                # Extract abstract
                abstract = top_result.find('div', class_='gs_rs').text.strip()
                
                # Construct the explanation
                explanation = f"Title: {title}\nAuthors: {authors}\nYear: {year}\nAbstract: {abstract}\nLink: {link}"
                return explanation
            else:
                return "No academic papers found for this query."
        else:
            return "Failed to retrieve search results."
    except Exception as e:
        return f"An error occurred: {e}"



def extract_abstract(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            abstract_tag = soup.find('div', class_='gs_rs')
            if abstract_tag:
                return abstract_tag.text.strip()
            else:
                return "No abstract found."
        else:
            return "Failed to retrieve paper content."
    except Exception as e:
        return f"An error occurred: {e}"

def summarize_text(text):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)
    # Extract the first few sentences as the summary
    summary = ' '.join(sentences[:2])  # Adjust the number of sentences as needed
    return summary

def summarize_google_scholar(query):
    try:
        # Perform search on Google Scholar
        url = f"https://scholar.google.com/scholar?q={query}"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            results = soup.find_all('div', class_='gs_r gs_or gs_scl')
            if results:
                print(f"Summaries for search results on '{query}':")
                for result in results:
                    title = result.find('h3', class_='gs_rt').text.strip()
                    abstract = result.find('div', class_='gs_rs').text.strip()
                    print(f"Title: {title}")
                    print(f"Abstract: {summarize_text(abstract)}")
                    print()
            else:
                print("No academic papers found for this query.")
        else:
            print("Failed to retrieve search results.")
    except Exception as e:
        print("An error occurred:", e)


def conduct_quiz_and_flashcards(topic):
    print(f"Generating quiz and flashcards for the topic: {topic}")
    
    # Example questions and answers (Replace this with dynamic generation based on the topic)
    quiz_questions = {
        "What is the primary function of the OSI model's Application Layer?": "Facilitate application services for file transfers, email, and other network software services.",
        # Add more questions based on the topic
    }

    flashcards = []
    
    # Conduct the quiz
    for question, answer in quiz_questions.items():
        user_answer = input(question + " ")
        if user_answer.lower() == answer.lower():
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is: {answer}")
        
        # Generate flashcard
        flashcards.append({"question": question, "answer": answer})
    
    # Optionally, display or do something with the generated flashcards
    print("\nGenerated Flashcards:")
    for flashcard in flashcards:
        print(f"Q: {flashcard['question']}")
        print(f"A: {flashcard['answer']}")
        print("---")



def calculate(expression):
    """Takes a mathematical expression as a string, converts it to a symbolic 
    expression using SymPy, and evaluates it."""
    try:
        x = Symbol('x')  # Define a symbolic variable (can be changed)
        expr = sp.sympify(expression)  # Convert string to symbolic expression
        result = expr.evalf()  # Evaluate the expression numerically
        return result
    except:
        return "Invalid expression."



# Main dialog function    
def chat():
    print("Hello, I'm learner! How can I help you with your schoolwork today?")
    
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
            explanation = explain(query)
            print("ResearchBot:", explanation)
            
        
        elif 'summary' in text:
                # Summarize Google Scholar search results
                query = input("What topic would you like to summarize? ").strip()
                summarize_google_scholar(query)
                
        
        
        elif 'quiz' in text or 'flashcards' in text:
            topic = input("What topic would you like to quiz yourself on or create flashcards for? ").strip()
            conduct_quiz_and_flashcards(topic)
            
        
        elif 'quit' in text or 'stop' in text or 'exit' in text:
            print("Thanks for chatting with me! Have a great day.")
            break
        
        elif 'math' in text:
            expression = text.split('math')[-1].strip()
            result = calculate(expression)
            print("ResearchBot: Result =", result)
            
        
        else:
            print("ResearchBot: I'm sorry, I don't understand. Please ask me a question about research, assignments, or studying!")
            


# Start chatbot      
chat()