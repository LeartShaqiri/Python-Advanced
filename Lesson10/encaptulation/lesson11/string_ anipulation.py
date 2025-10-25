# Read and clean each line from example.txt
with open("example.txt", "r") as file:
    for line in file:
        cleaned_line = line.strip()  # remove extra spaces/newlines
        print(cleaned_line)

# Read and split words from each line
with open("example.txt", "r") as file:
    for line in file:
        words = line.strip().split()
        print(words)

# Write name and age into output.txt (normal string format)
name = "drin"
age = 17

with open("output.txt", "w") as file:
    file.write("Name: " + name + "\n")
    file.write("Age: " + str(age) + "\n")

# Write name and age using f-strings (cleaner way)
with open("output.txt", "a") as file:  # 'a' = append so it doesn’t overwrite previous text
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")

# Read from example.txt and write to output.txt after modifying lines
with open("example.txt", "r") as infile, open("output.txt", "a") as outfile:
    for line in infile:
        cleaned_line = line.strip()
        modified_line = cleaned_line.replace("old_word", "new_word")
        outfile.write(modified_line + "\n")
