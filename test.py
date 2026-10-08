shots = [
    {
        "club": "7 iron",
        "distance": 145,
        "result": "good"
    },
    {
        "club": "7 iron",
        "distance": 150,
        "result": "good"
    },
    {
        "club": "7 iron",
        "distance": 138,
        "result": "thin"
    }
]

total_distance = sum(shot["distance"] for shot in shots)
total_shots = len(shots)
average_distance = total_distance / total_shots

print(f"Average distance: {average_distance:.1f} yards")    
print(f"Total distance: {total_distance:.1f} yards")

