#file_path = " example.txt"
#file = open (file_path.strip(), "r")
#content = file.read()
#print(content)
#file.close()


import os 




with open ("example.txt", "w") as file:
    file.write("hellow, world.\n")


lines = ["first line\n", "second line\n", "third line\n"]
with open ("example.txt", "w") as file:
    file.writelines(lines)

if os.path.exists("example.txt"):
    print("file found")

with open("example.txt", "a" ) as file:
    file.write("New")