import tkinter as tk
from tkinter import messagebox
import random

# Predefined questions
questions = [
    {
        "topic": "Loops", 
        "question": "What will be the output of this Python code?", 
        "code": "for i in range(3):\n    print(i)", 
        "options": ["0 1 2", "1 2 3", "0 1 2 3", "1 2"], 
        "answer": 0
    },

    {  
        "topic": "Loops", 
        "question": "How many times will this loop run?", 
        "code": "for i in range(1, 5):\n    print(i)", 
        "options": ["3", "4", "5", "Infinite"], 
        "answer": 1
    },
    
    {
        "topic": "Loops",
        "question": "What will the following code output?",
        "code": "x = 0\nwhile x < 3:\n    print(x)\n    x += 1",
        "options": ["0 1 2", "1 2 3", "0 1 2 3", "Error"],
        "answer": 0
    },

    {
        "topic": "Strings", 
        "question": "What does the following code output?", 
        "code": "'Python' + 'Quiz'", 
        "options": ["Python Quiz", "PythonQuiz", "Error", "None"], 
        "answer": 1
    },

    {
        "topic": "Strings",
        "question": "What will the output of this code be?",
        "code": "'hello'.upper()",
        "options": ["hello", "HELLO", "Hello", "Error"],
        "answer": 1
    },

    {
        "topic": "Strings",
        "question": "What will this print?",
        "code": "len('Hello World')",
        "options": ["11", "10", "12", "Error"],
        "answer": 0
    },

    {
        "topic": "Lists", 
        "question": "What will the following code output?", 
        "code": "list = [1, 2, 3]\nlist.append(4)\nprint(list)", 
        "options": ["[1, 2, 3]", "[1, 2, 3, 4]", "[4, 3, 2, 1]", "Error"],
        "answer": 1
    },

    {
        "topic": "Lists",
        "question": "What will this code return?",
        "code": "list = [5, 10, 15]\nprint(list[1])",
        "options": ["5", "10", "15", "Error"],
        "answer": 1
    },

    {
        "topic": "Lists",
        "question": "What will happen when this code runs?",
        "code": "list = [1, 2, 3]\nlist.pop()\nprint(list)",
        "options": ["[1, 2, 3]", "[1, 2]", "[2, 3]", "Error"],
        "answer": 1
    }
]

# Function to generate a question
def generate_question():
    topic = topic_entry.get().strip()
    matching_questions = [q for q in questions if q["topic"].lower() == topic.lower()]
    
    if not matching_questions:
        messagebox.showerror("Error", "No questions found for this topic!")
        return
    
    global current_question
    current_question = random.choice(matching_questions)
    
    # Display question details
    topic_label.config(text=f"Topic: {current_question['topic']}")
    question_label.config(text=f"Question: {current_question['question']}")
    code_label.config(text=f"Code:\n{current_question['code']}")
    
    # Clear feedback message
    feedback_label.config(text="")
    
    # Clear previous options
    for button in option_buttons:
        button.destroy()
    option_buttons.clear()
    
    # Reset the selected option
    selected_option.set(-1)  # Set to a value not corresponding to any answer
    
    # Add new options
    for idx, option in enumerate(current_question["options"]):
        btn = tk.Radiobutton(options_frame, text=option, variable=selected_option, value=idx, anchor="w")
        btn.pack(fill="x", padx=10, pady=2)
        option_buttons.append(btn)

# Function to check the answer
def check_answer():
    if current_question is None:
        messagebox.showerror("Error", "No question generated yet!")
        return
    
    selected = selected_option.get()
    if selected == -1:  # No option selected
        messagebox.showerror("Error", "Please select an option!")
        return
    
    if selected == current_question["answer"]:
        feedback_label.config(text="Correct! Well done!", fg="green")
    else:
        feedback_label.config(text="Incorrect. Try again.", fg="red")

# Initialize GUI
root = tk.Tk()
root.title("Python Quiz Generator")

# Set window size
root.geometry("600x450") 

# Input for topic
tk.Label(root, text="Enter Python Topic: (Lists, Strings, or Loops)").pack(pady=5)
topic_entry = tk.Entry(root)
topic_entry.pack(pady=5)

# Generate Question Button
generate_btn = tk.Button(root, text="Generate Python Question", command=generate_question)
generate_btn.pack(pady=5)

# Display Area
topic_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
topic_label.pack(pady=5)

question_label = tk.Label(root, text="", wraplength=500, justify="left")
question_label.pack(pady=5)

code_label = tk.Label(root, text="", font=("Courier", 10), wraplength=500, justify="left")
code_label.pack(pady=5)

# Options Area
options_frame = tk.Frame(root)
options_frame.pack(pady=5)
selected_option = tk.IntVar(value=-1)  # Default to an invalid value
option_buttons = []

# Submit Button
submit_btn = tk.Button(root, text="Submit", command=check_answer)
submit_btn.pack(pady=5)

# Feedback Area
feedback_label = tk.Label(root, text="", font=("Arial", 12, "italic"))
feedback_label.pack(pady=10)

# Start with no question selected
current_question = None

# Run the application
root.mainloop()