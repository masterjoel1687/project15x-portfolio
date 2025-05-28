note = input("Write a note: ")

# Save the note to notes.txt
with open("notes.txt", "a", encoding="utf-8") as file:
    file.write(note + "\n")

print("\nAll notes so far:")
# Read and display all notes
with open("notes.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())