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

for shot in shots:
    print("Club:", shot["club"])
    print("Distance:", shot["distance"], "yards")
    print("Result:", shot["result"])
    print() 
    