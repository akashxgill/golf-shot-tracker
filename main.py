def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def show_summary(club, distances, average):
    print("\nShot summary")
    print("Club:", club)
    print("Distances:", distances)
    print("Average distance:", average, "yards")

club = input("What club did you use? ")

distances = []

while True:
    user_input = input("How far was the shot? Type 'done' when finished: ")

    if user_input.lower() == "done":
        break

    try:
        distance = int(user_input)
        distances.append(distance)
    except ValueError:
        print("Please enter a number or type 'done'.")

average_distance = calculate_average(distances)

show_summary(club, distances, average_distance)