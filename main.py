def calculate_average(numbers):
    return sum(numbers) / len(numbers)


def calculate_range(numbers):
    return max(numbers) - min(numbers)


def show_summary(club, distances, average, distance_range):
    print("\nShot summary")
    print("Club:", club)
    print("Distances:", distances)
    print("Average distance:", average, "yards")
    print("Distance range:", distance_range, "yards")


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


if len(distances) == 0:
    print("No shots were entered.")
else:
    average_distance = calculate_average(distances)
    distance_range = calculate_range(distances)

    show_summary(club, distances, average_distance, distance_range)