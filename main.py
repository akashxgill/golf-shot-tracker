club = input("What club did you use? ")

distance1 = int(input("How far was shot 1? "))
distance2 = int(input("How far was shot 2? "))
distance3 = int(input("How far was shot 3? "))

average_distance = (distance1 + distance2 + distance3) / 3

print("\nShot summary")
print("Club:", club)
print("Shot 1:", distance1, "yards")
print("Shot 2:", distance2, "yards")
print("Shot 3:", distance3, "yards")
print("Average distance:", average_distance, "yards")
