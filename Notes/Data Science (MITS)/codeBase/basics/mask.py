score = int(input("Enter the score: "))

is_passing = (score > 40)
is_perfect = (score >= 100)

print("Final score bonus: ",10*is_passing + 50*is_perfect)
