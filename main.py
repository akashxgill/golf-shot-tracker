club = input("What club did you use? ")

distances = [
    int(input("How far was shot 1? ")),
    int(input("How far was shot 2? ")),
    int(input("How far was shot 3? "))
]

average_distance = sum(distances) / len(distances)

print("\nShot summary")
print("Club:", club)
print("Distances:", distances)
print("Average distance:", average_distance, "yards")
