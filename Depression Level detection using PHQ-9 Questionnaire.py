# PHQ-9 Questionnaire
questions = [
    "Over the last two weeks, how often have you been bothered by any of the following problems?\nLittle interest or pleasure in doing things?",
    "Feeling down, depressed, or hopeless?",
    "Trouble falling or staying asleep, or sleeping too much?",
    "Feeling tired or having little energy?",
    "Poor appetite or overeating?",
    "Feeling bad about yourself, underestimate yourself or that you are a failure or have let yourself or your family down?",
    "Trouble concentrating on things, such as reading the newspaper or watching television?",
    "Moving or speaking so slowly that other people could have noticed? Or the opposite - being so fidgety or restless that you have been moving around a lot more than usual?",
    "Thoughts that you would be better off dead, or of hurting yourself in some way?"
]

choices = ["Not at all", "Several days", "More than half the days", "Nearly every day"]

# Function to generate the quiz
def generate_quiz(questions, choices):
    quiz = []
    for i, question in enumerate(questions, start=1):
        print(f"Question {i}: {question}")
        for j, choice in enumerate(choices, start=1):
            print(f"{j}. {choice}")
        answer = input("Enter your choice (1-4): ")
        quiz.append((question, choices[int(answer) - 1]))
    return quiz

# Generate the Quiz
quiz = generate_quiz(questions, choices)

# Calculate total score
total_score = sum([min(choices.index(answer), 3) for _, answer in quiz])

# Determine depression level
depressionLevel = ""
if total_score >= 0 and total_score <= 4:
    depressionLevel = "none"
elif total_score >= 5 and total_score <= 9:
    depressionLevel = "mild"
elif total_score >= 10 and total_score <= 14:
    depressionLevel = "moderate"
elif total_score >= 15 and total_score <= 19:
    depressionLevel = "moderately severe"
elif total_score >= 20:
    depressionLevel = "severe"

# Display total score and depression level
print(f"Total Score: {total_score}/27")
print(f"Depression Level: {depressionLevel}")

# Save the quiz answers and score to a file
file_path = "/G:\depression level/phq9_quiz_answers.txt"
with open("phq9_quiz_answers.txt", "w") as file:
    for question, answer in quiz:
        file.write(f"{question}\nAnswer: {answer}\n\n")
    file.write(f"Total Score: {total_score}/27\n")
    file.write(f"Depression Level: {depressionLevel}\n")

# Read the quiz answers and total score from the file
with open("phq9_quiz_answers.txt", "r") as file:
    content = file.read()

# Print the contents of the file
print(content)
