import csv
import random
from datetime import datetime

# Score variables
total_score = 0
correct_answers = 0
wrong_answers = 0

def guessTheYear():
    global total_score, correct_answers, wrong_answers

    events = []
    with open("timeline.csv", "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # skip header row
        for row in csv_reader:
            events.append(row)

    if not events:
        print("No events found in the file.")
        return

    random_event = random.choice(events)
    year = random_event[0].split("-")[0].strip()
    event = random_event[1].strip()

    print(f"Guess the year of the event: {event} \n")
    guess = input("Enter your guess (or type 'exit' to quit): ").strip()
    if guess.lower() == "exit":
        return "exit"

    total_score += 1
    if guess == year:
        print("✅ Correct!")
        correct_answers += 1
    else:
        print(f"❌ Wrong! The correct year was {year}.")
        wrong_answers += 1
    print(f"Current Score → {correct_answers} correct, {wrong_answers} wrong, {total_score} total\n")

def beforeOrAfter():
    global total_score, correct_answers, wrong_answers

    events = []
    with open("timeline.csv", "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # skip header row
        for row in csv_reader:
            events.append(row)

    if len(events) < 2:
        print("Not enough events to play this quiz.")
        return

    event_a, event_b = random.sample(events, 2)
    year_a = int(event_a[0].split("-")[0])
    year_b = int(event_b[0].split("-")[0])
    text_a = event_a[1]
    text_b = event_b[1]

    print(f"Event A: {text_a}")
    print(f"Event B: {text_b}")
    answer = input("Did Event A happen before or after Event B? (type 'exit' to quit): ").strip().lower()
    if answer == "exit":
        return "exit"

    total_score += 1
    if (answer == "before" and int(year_a) < int(year_b)) or \
       (answer == "after" and int(year_a) > int(year_b)):
        print("✅ Correct!")
        correct_answers += 1
    else:
        print(f"❌ Wrong! Event A happened in {year_a} and Event B in {year_b}.")
        wrong_answers += 1
    print(f"Current Score → {correct_answers} correct, {wrong_answers} wrong, {total_score} total\n")

# --- Main Program ---
player_name = input("Enter your name: ")
print(f"Hello, {player_name}! Welcome to Kenya History Quiz.\n")

while True:
    print("\nChoose the option below:")
    print("1. Guess the Year")
    print("2. Before or After")
    print("Type 'exit' to quit.")

    choice = input("Enter your choice: ").strip().lower()
    if choice == "exit":
        break
    elif choice == "1":
        result = guessTheYear()
        if result == "exit":
            break
    elif choice == "2":
        result = beforeOrAfter()
        if result == "exit":
            break
    else:
        print("Invalid choice. Please select a valid option.")


# Final score summary
print("\n--- Quiz Summary ---")
print(f"Total Questions: {total_score}")
print(f"Correct Answers: {correct_answers}")
print(f"Wrong Answers: {wrong_answers}")
