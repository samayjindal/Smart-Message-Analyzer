import pandas as pd

# Load dataset (just for project purpose)
data = pd.read_csv("spam.csv", encoding='latin-1')

# Keep only useful columns
data = data[['v1', 'v2']]
data.columns = ['label', 'message']


# Function to analyze message
def analyze_message(msg):
    msg = msg.lower()

    # spam-related words
    spam_keywords = ["win", "free", "offer", "money", "urgent", "click"]

    # study-related words
    study_keywords = ["study", "exam", "notes", "motivation"]

    # Check for spam
    for word in spam_keywords:
        if word in msg:
            return "🚨 Spam Detected! This message may be unsafe."

    # Check for study related query
    for word in study_keywords:
        if word in msg:
            return "📚 Study Tip: Stay consistent and revise daily."

    # Default case
    return "🙂 This seems like a normal message."


# Main program (runs when file is executed)
if __name__ == "__main__":
    print("=== Smart Message Analyzer ===")
    
    user_input = input("Enter your message: ")
    
    result = analyze_message(user_input)
    
    print("Result:", result)