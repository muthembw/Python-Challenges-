Player_name = input("Enter your name: ").strip()
print(f"Hello, {Player_name}! Welcome to the Cyber Security Quiz! \n")

def start_quiz():
    print(f"\nYour total score is: {total_score}")
    print(f"\nCorrect answers: {correct_answers}")
    print(f"\nWrong answers: {wrong_answers}")

total_score = 0
correct_answers = 0
wrong_answers = 0
quiz = [
    {
        "Question": "What is the primary purpose of a firewall?",
        "Options": [
            "A: To encrypt user data",
            "B: To detect malware on a computer",
            "C: To block unauthorized access to or from a network",
            "D: To manage user passwords"
        ],
        "Answer": "C. To block unauthorized access to or from a network"
    },
    {
        "Question": "Which of the following is an example of a strong password?",
        "Options": [
            "A: password123",
            "B: John2020",
            "C: M$kL9@r!2#zP",
            "D: qwerty"
        ],
        "Answer": "C. M$kL9@r!2#zP"
    },
    {
        "Question": "Phishing attacks are primarily aimed at",
        "Options": [
            "A: Infecting systems with ransomware",
            "B: Physically stealing computers",
            "C: Tricking users into revealing personal information",
            "D: Overloading websites with traffic"
        ],
        "Answer": "C. Tricking users into revealing personal information"
    },
    {
        "Question": "Which of these is a form of malware that locks or encrypts a victim’s files until a ransom is paid?",
        "Options": [
            "A: Adware",
            "B: Ransomware",
            "C: Spyware",
            "D: Trojan"
        ],
        "Answer": "B. Ransomware"
    },
    {
        "Question": "What does the principle of “least privilege” refer to in cybersecurity?",
        "Options": [
            "A: Users should have only the access necessary to perform their job functions.",
            "B: All users should have administrative access.",
            "C: Users should be allowed to install any software they want.",
            "D: Access rights should be granted based on seniority."
        ],
        "Answer": "A. Users should have only the access necessary to perform their job functions."
    },
    {
        "Question": "What is the role of encryption in cybersecurity?",
        "Options": [
            "A: To protect data confidentiality",
            "B: To ensure data integrity",
            "C: To provide authentication",
            "D: All of the above"
        ],
        "Answer": "D. All of the above"
    },
    {
        "Question": "What is a zero-day vulnerability?",
        "Options": [
            "A: A malware that activates after 24 hours",
            "B: A vulnerability that has been patched already",
            "C: A newly discovered vulnerability that is not yet known to the software vendor",
            "D: A virus with no known origin"
        ],
        "Answer": "C. A newly discovered vulnerability that is not yet known to the software vendor"
    }
]
security_tips = {
    0: "A firewall helps prevent unauthorized access. Always keep it enabled.",
    1: "Strong passwords are long and use symbols, numbers, and upper/lowercase letters.",
    2: "Never click unknown links or attachments; phishing attacks trick users into giving away info.",
    3: "Ransomware encrypts your data. Always backup files and avoid suspicious downloads.",
    4: "Only give users the access they need. 'Least privilege' reduces damage from attacks.",
    5: "Encryption secures your data during transmission. Always enable HTTPS and device encryption.",
    6: "Zero-day vulnerabilities are dangerous. Keep systems updated with patches."
}

i = 0
while i < len(quiz):
    print(quiz[i]["Question"])
    for Option in quiz[i]["Options"]:
        print(Option)
    while True:
        answer = input("\nEnter your answer or type 'quit' to exit: ")
        if answer.strip().lower() == "quit":
            print("Quiz ended by user.")
            exit()
        if answer not in ["a", "b", "c", "d"]:
            print("Please enter a valid answer: A, B, C, or D.")
            continue
        elif answer.strip().lower() == quiz[i]["Answer"].split(".")[0].strip().lower():
            print("Correct! ✅")
            total_score += 5
            correct_answers += 1
        else:
            print(f" \nIncorrect. The correct answer is: {quiz[i]['Answer']} \n")
            print(f"Security Tip: {security_tips[i]} \n")
            wrong_answers += 1
        break
    i += 1
start_quiz()