# AI Study Buddy : Rule Based Chat Assistant in Python

import datetime


# Function for greeting according to current time
def get_greeting():
    hour = datetime.datetime.now().hour

    if 5 <= hour < 12:
        return "Good Morning"
    elif 12 <= hour < 17:
        return "Good Afternoon"
    elif 17 <= hour < 21:
        return "Good Evening"
    else:
        return "Good Night"


# Function to get current time
def get_time():
    current_time = datetime.datetime.now()
    return current_time.strftime("%I:%M %p")


# Function to get today's date
def get_date():
    current_date = datetime.datetime.now()
    return current_date.strftime("%d %B %Y")


# Chatbot responses
responses = {

    "hello": "Hi! Welcome to Study Buddy. How can I help you?",

    "hi": "Hello! What would you like to study today?",

    "how are you":
        "I am doing great and ready to help you study!",

    "who are you":
        "I am Study Buddy, a simple rule-based Python chatbot.",

    "what can you do":
        "I can give study tips, motivation, exam advice and tell you the time and date.",

    "motivate me":
        "Keep going! Every small step you take today makes you better tomorrow.",

    "i am tired":
        "Take a short break, drink some water and then start again with a small task.",

    "i am stressed":
        "Don't try to finish everything at once. Pick one small topic and focus on it.",

    "i am lazy":
        "Start with just 10 minutes. Once you begin, studying becomes easier.",

    "study tip":
        "Try studying for 25 minutes and then take a 5-minute break.",

    "how to study":
        "Make a small plan, remove distractions, study actively and revise regularly.",

    "exam preparation":
        "Start with important topics, practice questions and revise regularly.",

    "focus":
        "Keep your phone away, choose one task and study for 25 minutes without distractions.",

    "thank you":
        "You're welcome! I am always happy to help.",

    "thanks":
        "You're welcome! Keep learning!"
}


# Function to get response from chatbot
def get_bot_response(user_question):

    user_question = user_question.lower().strip()

    # Exit commands
    if user_question in ["bye", "exit", "quit"]:
        return "Goodbye! Keep learning and keep growing!"

    # Time
    if "time" in user_question:
        return f"The current time is {get_time()}."

    # Date
    if "date" in user_question or "today" in user_question:
        return f"Today's date is {get_date()}."

    # Check the questions stored in dictionary
    for eachkey in responses:
        if eachkey in user_question:
            return responses[eachkey]

    # If question is not available
    return "I don't know that yet. Try asking me about study tips, exams, motivation or time."


# Main program

print("=" * 45)
print("        AI STUDY BUDDY")
print("     Rule Based Chat Assistant")
print("=" * 45)

name = input("\nWelcome to Study Buddy! Enter your name: ").strip()

if name == "":
    name = "Student"

print(f"\n{get_greeting()}, {name}!")

print("\nI can help you with:")
print("- Study tips")
print("- Exam preparation")
print("- Motivation")
print("- Focus")
print("- Time and date")

print("\nType 'bye' to exit the chatbot.")


while True:

    user_input = input(f"\n{name}: ").strip()

    if user_input == "":
        print("Study Buddy: Please type something.")
        continue

    reply = get_bot_response(user_input)

    print("Study Buddy:", reply)

    if user_input.lower() in ["bye", "exit", "quit"]:
        print("BYE BYE!!")
        break
