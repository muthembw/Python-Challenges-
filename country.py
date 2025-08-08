import random
import csv

def play_round(random_country):
    print("\nNew Round!")
    print("The country selected has", len(random_country), "letters.")
    first_letter = random_country[0]
    guessed_letters = [first_letter] + ["_"] * (len(random_country) - 1)
    print("Clue: " + " ".join(guessed_letters))

    score = 0
    for i in range(1, len(random_country)):
        player_guess = input(f"Guess letter {i+1}: ").strip()
        correct_letter = random_country[i]

        if player_guess.lower() == correct_letter.lower():
            guessed_letters[i] = correct_letter
            print("✅ Correct! " + " ".join(guessed_letters))
            score += 1
        else:
            guessed_letters[i] = correct_letter
            print(f"❌ Incorrect. The correct letter was '{correct_letter}'")
            print("Revealed: " + " ".join(guessed_letters))
    print(f"🎯 You completed the word: {random_country}")
    print(f"Score this round: {score}")
    return score

def save_to_leaderboard(player_name, total_score, filename="Leaderboard.csv"):
    with open(filename, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([player_name, total_score])
def display_leaderboard(filename="Leaderboard.csv"):
    try:
        with open(filename, mode="r", newline="") as file:
            reader = csv.reader(file)
            leaderboard = sorted(reader, key=lambda row: int(row[1]), reverse=True)
            print("\n🏆 Leaderboard (Top Scores):")
            for rank, entry in enumerate(leaderboard, 1):
                print(f"{rank}. {entry[0]} - {entry[1]} points")
    except FileNotFoundError:
        print("Leaderboard file not found.")

def start_game():
    player_name = input("Enter your name: ").strip()
    print(f"Hello, {player_name}! Welcome to the Country Quiz Game 🌍")
    print("You will be guessing country names one letter at a time.")
    print("Let's begin!\n")

    countries = [
        "Kenya", "Uganda", "Tanzania", "Rwanda", "Burundi", "South Sudan", "Somalia",
        "Ethiopia", "Djibouti", "Eritrea", "Sudan", "South Africa", "Zimbabwe", "Zambia",
        "Malawi", "Mozambique", "Angola", "Namibia", "Botswana", "Europe", "Germany",
        "France", "Italy", "Spain", "Portugal", "Netherlands", "Belgium", "Sweden","India",
        "China", "Japan", "South Korea", "North Korea", "Vietnam", "Thailand", "Malaysia", 
        "Norway", "Finland", "Denmark", "Poland", "Czech Republic", "Slovakia", "Hungary",
        "Austria", "Switzerland", "Greece", "Turkey", "Liechtenstein", "Luxembourg", "Malta",
        "Iceland", "Ireland", "United Kingdom", "Russia", "Ukraine", "Belarus", "Lithuania", 
        "Latvia", "Estonia", "Moldova", "Romania", "Bulgaria", "Serbia", "Croatia", "Bosnia and Herzegovina",
          "Montenegro", "North Macedonia", "Albania", "Kosovo", "Slovenia", "Egypt", "Libya", "Tunisia", "Algeria",
            "Morocco", "Western Sahara", "Mauritania", "Mali", "Niger", "Chad", "Cameroon", "Central African Republic", 
            "Gabon", "Republic of the Congo", "Democratic Republic of the Congo","Iran", "Iraq", "Syria", "Lebanon", "Jordan",
    ]

    selected_countries = random.sample(countries, 10) 
    total_score = 0

    for country in selected_countries:
        round_score = play_round(country)
        total_score += round_score

    print(f"\n🎉 Game Over! {player_name}, your total score is: {total_score} points.")

    save_to_leaderboard(player_name, total_score)
    print("Your score has been saved to the leaderboard.")

# Start the game
start_game()
