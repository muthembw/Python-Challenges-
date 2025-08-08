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

def start_game():
    player_name = input("Enter your name: ").strip()
    print(f"Hello, {player_name}! Welcome to the Country Quiz Game 🌍")
    print("You will be guessing country names one letter at a time.")
    print("Let's begin!\n")

    countries = [
        "Kenya", "Uganda", "Tanzania", "Rwanda", "Burundi", "South Sudan", "Somalia",
        "Ethiopia", "Djibouti", "Eritrea", "Sudan", "South Africa", "Zimbabwe", "Zambia",
        "Malawi", "Mozambique", "Angola", "Namibia", "Botswana", "Europe", "Germany",
        "France", "Italy", "Spain", "Portugal", "Netherlands", "Belgium", "Sweden",
        "Norway", "Finland", "Denmark", "Poland", "Czech Republic", "Slovakia", "Hungary",
        "Austria", "Switzerland", "Greece", "Turkey"
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
