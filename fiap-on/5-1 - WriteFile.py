with open("text.txt", "w") as file:
    file.write("Creating a file with Python")
with open("text.txt", "w") as file:
    file.write("\n Another info")
with open("text.txt", "r") as file:
    content = file.read()
    print(content)