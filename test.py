club = input("What club did you use? ")

distances = []

while True:
    user_input = input("How far was the shot? Type 'done' when finished: ")

    if user_input.lower() == "done":
        break

    distance = int(user_input)
    distances.append(distance)

average_distance = sum(distances) / len(distances)

print("\nShot summary")
print("Club:", club)
print("Distances:", distances)
print("Average distance:", average_distance, "yards")
