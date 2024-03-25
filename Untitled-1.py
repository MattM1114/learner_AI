# this is were I will be showing the ai that I will make 
# 1st I need to import ,the important files 
# such as the nlp library and scholarly 
# Import NLP libraries
import nltk
import webbrowser
from nltk.stem import WordNetLemmatizer

# ths will lemmatize the query before searching
nltk.download('punkt') 
nltk.download('wordnet')


# Import library for academic search
import scholarly  

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
        results = scholarly.search_pubs(query)
        if results:
            # Iterate over results
            for i, result in enumerate(results):
                # Open browser to top result
                if i == 0:
                    webbrowser.open(result.bib['url'])
                    print("Academic paper opened in your default browser.")
                
                # Print out some key info for each result
                print("Result", i+1)
                print("Title:", result.bib['title'])
                print("Author:", result.bib['author'])
                print("Year:", result.bib['year'])
                print("URL:", result.bib['url'])
                print()
        else:
            print("No academic papers found for this query.")
    except Exception as e:
        print("An error occurred:", e)



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
        
        elif 'summary' in text:
            # Call summarization function
            pass
        
        else:
            print("ResearchBot: I'm sorry, I don't understand. Please ask me a question about research, assignments, or studying!")


# Start chatbot      
chat()
