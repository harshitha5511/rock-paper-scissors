import random

choices = ["rock", "paper", "scissors"]

print("🎮 Rock Paper Scissors Game")
print("Type rock, paper, or scissors")

user_score = 0
computer_score = 0

while True:
    user = input("\nYour choice: ").lower()

    if user == "exit":
        print("Thanks for playing!")
        break

    if user not in choices:
        print("Invalid choice!")
        continue

    computer = random.choice(choices)

    print("Computer chose:", computer)

    if user == computer:
        print("🤝 It's a Tie!")
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        print("🎉 You Win!")
        user_score += 1
    else:
        print("😢 Computer Wins!")
        computer_score += 1

    print(f"Score → You: {user_score} | Computer: {computer_score}")


