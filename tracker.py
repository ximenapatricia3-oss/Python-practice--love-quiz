print("=" * 50)
print("       ✨ THE ULTIMATE LOVE QUIZ FOR COLTON ✨       ")
print("=" * 50 + "\n")

score = 0

# Question 1
ans1 = input("1. Who is the most amazing and beautiful girl in the world?\nYour answer: ").strip().lower()
if "ximena" in ans1:
    print("Correct! Point for love!\n")
    score += 1
else:
    print("Hmm... incorrect answer, but we'll let it slide!\n")

# Question 2 (Opciones actualizadas)
ans2 = input("2. What is Ximena and Colton's favorite activity together? (Type 'shopping', 'eating out', 'watching movies' or 'coding'):\nYour answer: ").strip().lower()
if "shopping" in ans2 or "eating out" in ans2 or "watching movies" in ans2 or "coding" in ans2:
    print("Spot on! All of the above count!\n")
    score += 1
else:
    print("Interesting answer, noted!\n")

# Question 3
ans3 = input("3. From 1 to 10, how much is Colton in love with Ximena? (Type a number):\nYour answer: ")
print("Answer successfully recorded!\n")
score += 1 # ¡Punto libre por honestidad!

# Question 4
ans4 = input("4. Who is the better cook? (Ximena / Colton):\nYour answer: ").strip().lower()
if "ximena" in ans4:
    print("Haha, totally agree!\n")
else:
    print("Secret kitchen genius! We'll keep that between us...\n")
score += 1

# Question 5
ans5 = input("5. What does Colton love the most about Ximena? (Her smile, her heart, or her intelligence?):\nYour answer: ").strip().lower()
print("Aww, that's definitely true!\n")
score += 1

# Question 6
ans6 = input("6. Are you ready to give Ximena a giant hug right now? (yes/no):\nYour answer: ").strip().lower()
if "yes" in ans6:
    print("Excellent answer! Green light for a hug.\n")
    score += 1
else:
    print("Oops, that answer is not allowed, go hug her anyway!\n")

# Final Result
print("=" * 50)
print(f"       FINAL SCORE: {score} / 6 POINTS       ")
print("=" * 50)

if score >= 5:
    print("Congratulations Colton! You unlocked the highest level in Ximena's heart ❤️")
else:
    print("You still win because the grand prize is all of Ximena's love! 🥰")

input("\nPress Enter to exit...")
