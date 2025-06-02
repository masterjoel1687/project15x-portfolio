note = input("Write a note: ")

with open("notes.txt", "a", encoding="utf-8") as file:
    file.write(note + "\n")

print("\nAll notes so far:")

with open("notes.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
        