const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Function to interact with the chat and display responses
function chat() {
    console.log("Hello, I'm learner! How can I help you with your schoolwork today?");

    rl.question("You: ", function(text) {
        // Preprocess text
        text = preprocess(text);

        fetch("/query", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ query: text })
        })
            .then((response) => response.json())
            .then((data) => {
                console.log("ResearchBot:", data.response);
            })
            .catch((error) => {
                console.error("Error:", error);
            });
    });
}

// Start the chat when the script is executed
chat();