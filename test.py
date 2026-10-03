club = input("What club did you use? ")

distances = []

for shot in range(3):
    distance = int(input(f"How far was shot {shot + 1}? "))
    distances.append(distance)

average_distance = sum(distances) / len(distances)

print("\nShot summary")
print("Club:", club)
print("Distances:", distances)
print("Average distance:", average_distance, "yards")
