marks = {
    "Akshay": 92,
    "Anuj": 72,
    "Ronnie": 53
}

print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"Akshay": 99, "Shelby": 91})
print(marks)
print(marks.get("Akshay"))  # print(marks["Akshay"]) What is the difference

print(marks.get("Akshay2"))    # Prints None  
print(marks["Akshay2"])        # Returns Error