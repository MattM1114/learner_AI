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





# Function to provide explanations or summaries
def provide_explanation(query):
    try:
        # Perform search on Google Scholar
        url = f"https://scholar.google.com/scholar?q={query}"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            results = soup.find_all('div', class_='gs_r gs_or gs_scl')
            if results:
                # Get the title and abstract of the top result
                top_result = results[0]
                title = top_result.find('h3', class_='gs_rt').text.strip()
                abstract = top_result.find('div', class_='gs_rs').text.strip()
                explanation = f"Title: {title}\nAbstract: {abstract}"
                return explanation
            else:
                return "No academic papers found for this query."
        else:
            return "Failed to retrieve search results."
    except Exception as e:
        return f"An error occurred: {e}"


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
        
        elif 'summary' in text:
            # Extract the topic for summarization
            topic = text.split('summary')[-1].strip()
            # Call provide_explanation to get a summary
            summary = provide_explanation(topic)
            print("ResearchBot:", summary)
        
        
        elif 'quiz' in text or 'flashcards' in text:
            topic = input("What topic would you like to quiz yourself on or create flashcards for? ").strip()
            conduct_quiz_and_flashcards(topic)
        
        elif 'quit' in text or 'stop' in text or 'exit' in text:
            print("Thanks for chatting with me! Have a great day.")
            break
        
        
        else:
            print("ResearchBot: I'm sorry, I don't understand. Please ask me a question about research, assignments, or studying!")


# Start chatbot      
chat()
